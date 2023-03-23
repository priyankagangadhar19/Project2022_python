from typing import Set

a=10
b=4
c=a-b
print(c)

x=1.3
y=3.4
print(x-y)

p=5j
q=8j
print(p-q)

t=10
y=20.65
print(t-y) #int-float

print(10.54-5j) #float-complex

print(10-10j)

#print(10-abc) #number and string cannot be subtracted/added

# text=[1,2,3]
# text1=[2,3,4]
# result=text-text1

# text=(1,2,3)
# text1=(1,2,3)
# result=text-text1

s1={1,2,3,5,6}
s2={1,3}
result=s1-s2
print(s1.difference(s2))
print(s1-s2)

# d1={"string":23}
# d2={"stri":10}
# print(d1-d2)
s3={"a","b"}
s4={"b"}
print(s3.difference(s4))
print(s3-s4)

