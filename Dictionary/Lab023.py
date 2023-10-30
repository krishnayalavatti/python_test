api_response={
        "firstname": "Krishna",
        "lastname": "Yalavatti",
        "totalprice": 111,
        "depositpaid": "true",
        "additionalneeds": "Breakfast"
    }

print(api_response)
print(type(api_response))

print(api_response.get('totalprice'))
print(api_response['depositpaid'])


for key, value in api_response.items():
        print(key,value)
