class A:
    i=10


class B(A):
    j=100


class C(A):
    k=200

class D(B,C):
    pass

print(D.i)
print(D.j)
print(D.k)


#this is hybrib inheritance. includes all the inheritance concepts
