phone_book={"Batman":887766,"Superman":5544,"Wonder":55223311}

# Dict? It is very close to the JSON
# JSON- Key and Value

print(phone_book)
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Wonder"])

# You can access element by Key only - Dict

phone_book2=dict(Batman=123,Cersei=342,GB=323)
print(phone_book2)
print(phone_book2["GB"])
print(phone_book2['GB'])
print(phone_book2.get("GB"))


new_dic = dict(name="Krishna",age=25,Ismate=True,Address="NA")
print(new_dic)
print(new_dic['age'])
print(new_dic.get('age'))

new_dic2={"name":"Krishna",90:34,"Ismale":True,"Address": "NA"}
print(new_dic2)
print(new_dic2['name'])
print(new_dic2.get(90))