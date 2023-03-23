# print((lambda n: n*2)(100))
#
#
#
#
#
# def add(n,m):
#     return n+m
# res=add(10,20)
# print(res)
#
#
# def m1(n):
#     return n+1
#
# res=m1(10)
# print(res)
#
# #lambda args:expression

add=lambda n,m: n+m
res=add(10,20)
print(res)

#code optimization
print((lambda n,m : n+m) (10,20))


#check if number is positive or negative using lambda

#check if number is > 0 or not true or false
n=6
print((lambda n:n>0)(n))

#odd/even using lambda
n= 9
print((lambda n: n%2==0)(n))


n=5
print((lambda n:("even" if n%2==0 else "odd"))(n))


