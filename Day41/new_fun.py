#argument ---> store value in a variable
def fun1(a):
    res=a+a
    return res

v=fun1(10)
print(v)

m=fun1
v=m(10)
print(v)
