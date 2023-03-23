class A:
    i = 10

    def __init__(self,k):
        self.j = k

class B(A):
   def __init__(self,l):
       super().__init__(l)

class C(B):
    def __init__(self, m):
        super().__init__(m)

print(C.i)
obj=C(56)
print(obj.j)