#can we store method in another variable and call the method using new variable?-yes
def m1():
   print('hi')

m2=m1
m1()
m2()

print(type(m1))
print(type(m2))
