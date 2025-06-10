from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn


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

class ProductInput(BaseModel):
    name: str
    price: float
    quantity: int

class Product(HashModel):
    name : str
    price : float
    quantity : int

    class Meta:
        database = redis

@app.get('/products')
def get_products():
    return [format_product(pk) for pk in Product.all_pks()]

def format_product(pk : str):
    product = Product.get(pk)
    return {
        'Id' : product.pk,
        'Name' : product.name,
        'Price' : product.price,
        'Quantity' : product.quantity
    }

@app.post('/products')
def create_product(product : ProductInput):
    new_product = Product(**product.dict())
    return new_product.save()

@app.get('/products/{pk}')
def get_product(pk : str):
    return Product.get(pk)

@app.delete('/products/{pk}')
def delete_product(pk : str):
    return Product.delete(pk)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)


