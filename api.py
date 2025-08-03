api="http://localhost:3000/Products"
add={
    "name":"Poco"
}
add=json.dumps(add)
putdata=requests.patch(api,data=add)
print(putdata.json())
a=requests.delete(api)
print(a)

newdata=[
    {
    "id":"1",
    "name":"Iphone",
    "price":"1.5Lakhs"
    },
    {
        "id":"2",
        "name":"Watch",
        "price":"2k"
    },
    {
        "id":"3",
        "name":"Accessories",
        "price":"10k"

    }
    ]
for item in newdata:
    putdata = requests.post(api, data=json.dumps(item), headers={"Content-Type": "application/json"})
    print(putdata.status_code, putdata.json())
apidiscount="http://localhost:3000/discount"
products=[
    {
    "id":"1",
    "name":"Iphone",
    "discount":"50%"
    },
    {
        "id":"2",
        "name":"Watch",
        "discount":"20%"
    },
    {
        "id":"3",
        "name":"Accessories",
        "discount":"10%"

    }
]
for item in products:
    putdata=requests.post(apidiscount,data=json.dumps(item))
    print(putdata.json())
