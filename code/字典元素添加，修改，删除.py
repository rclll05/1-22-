a =  {'name':'rcl','age':18,'job':'programmer'}
a['address'] = '一号院'
a['age'] = 28
print(a)

a =  {'name':'rcl','age':18,'job':'programmer'}
b =  {'name':'rcg','age':6,'job':'student','gender':'men','money':1000}
a.update(b)
print(a)

a =  {'name':'rcl','age':18,'job':'programmer'}
b =  {'name':'rcg','age':6,'job':'student','gender':'men','money':1000}
a.update(b)
del(a['name'])
print(a)

a =  {'name':'rcl','age':18,'job':'programmer'}
b =  {'name':'rcg','age':6,'job':'student','gender':'men','money':1000}
a.update(b)
nianlin = a.pop('age')
print(a)
print(nianlin)
a.popitem()
print(a)
a.popitem()
print(a)
a.popitem()
print(a)
a.popitem()
print(a)