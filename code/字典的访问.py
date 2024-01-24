a =  {'name':'rcl','age':18,'job':'programmer'}
print(a['name'])
print(a.get("age"))
#print(a["gender"]) #报错
print(a.get("gender","man"))
print(a.items())
print(a.keys())
print(a.values())
print(len(a))
print("name" in a)