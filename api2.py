import requests
api='https://screenshotmax.com/'
data=requests.get(api)
products=data.json()
print(products)
import requests

api="https://fakestoreapi.in/api/products"
data=requests.get(api)
print(data.json())
api2='https://jsonplaceholder.typicode.com/posts'
data1=requests.get(api2)
print(data1.json())
send_data={
    'id':101,
    'title':'srivalli',
    'body':'python is great'
}
postdata=requests.post(api2,data=send_data)
print(postdata.json())
print(data1.json())
