a =  {'name':'rcl','age':18,'job':'programmer'}
print(a)
print(a['name'])

b = dict(name='rcl',age=18,job="programmer")
print(b)

c = dict([("name","rcl"),("age",18),("job","programmer")])
print(c)

k = ["name","age","job"]
v = ["rcl",18,"programmer"]
#print(list(zip(k,v)))
d = dict(zip(k,v))

f = dict.fromkeys(["name","age","job"])
print(f)