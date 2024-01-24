a = [x*10 for x in range(5)]
print(a)

b = (x*10 for x in range(5))
c = tuple(b)
print(c)
d = tuple(b)
print(d)
e = (x for x in range(3))
print(e.__next__())
print(e.__next__())
print(e.__next__())
#print(e.__next__()) 报错