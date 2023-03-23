class A:
    def __init__(self,x):
        self.i = x



class B:
    def __init__(self,y):
        self.i= y

class C(A,B):#  calll the constructor of all the parent classes. def __init--(self
    def __init__(self,p,q):
        A.__init__(self,p)
        B.__init__(self,q)

obj=C(10,20)
print(obj.__dict__)
print(obj.i)


#overrides the class B value and prints 20