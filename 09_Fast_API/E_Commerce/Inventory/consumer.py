from main import redis, Product
import time

key = 'order_complete'
group = 'inventory-group'

try:
    redis.xgroup_create(key, group)
except:
    print('Group already existed.')

while True:
    try:
        results = redis.xreadgroup(group, key, {key : '>'}, None)
        if results != []:
            for result in results:
                obj = result[1][0][1]
                try:
                    product = Product.get(obj['product_id'])
                    print(product)
                    product.quantity = product.quantity - int(obj['quantity'])
                    product.save()
                except:
                    redis.xadd('refund_order', obj, '*')
    except Exception as e:
        print(str(e))
    time.sleep(1)