class A:
    def __init__(self,i):
        self.i = i



class B:
    def __init__(self,j):
        self.j=j

class C(A,B):#  calll the constructor of all the parent classes. def __init--(self
    def __init__(self,i,j):
        A.__init__(self,i)
        B.__init__(self,j)

obj=C(10,70)
print(obj.__dict__)
print(obj.i)
print(obj.j)


