from fastapi import FastAPI
from fastapi.background import BackgroundTasks
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.requests import Request
import uvicorn, requests, time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*']
)

redis = get_redis_connection(
    host = 'redis-15817.c301.ap-south-1-1.ec2.redns.redis-cloud.com',
    port = 15817,
    password = 'VfJhnOEVQ2w5F0Tb8ijfRy0FBmzNm3Kq',
    decode_responses = True
)

class Order(HashModel):
    product_id : str
    price : float
    fee : float
    total : float
    quantity : int
    status : str

    class Meta:
        database = redis

@app.get('/orders/{id}')
def get_order(pk : str):
    return Order.get(pk)

@app.post('/orders')
async def create_order(request : Request, background_task : BackgroundTasks):
    body = await request.json()
    req = requests.get('http://localhost:9000/products/%s' % body['id'])
    product = req.json()
    order = Order(
        product_id = body['id'],
        price = product['price'],
        fee = 0.2 * product['price'],
        total = 1.2 * product['price'],
        quantity = body['quantity'],
        status = 'pending'
    )
    order.save()
    background_task.add_task(order_complete, order)
    return order

def order_complete(order : Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    redis.xadd('order_complete', order.dict(),'*')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9001, reload=True)


