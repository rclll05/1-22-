r1 = {'name':'rcl','age':18,'salary':30000,'city':'北京'}
r2 = {'name':'rcll','age':28,'salary':20000,'city':'广州'}
r3 = {'name':'rclll','age':38,'salary':10000,'citb[ty':'惠州'}

tb = [r1,r2,r3]
print(tb)
print(tb[1].get("salary"))

print(len(tb))

for i in range(len(tb)):
    print(tb[i].get("salary"))

for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("salary"),tb[i].get("city"))