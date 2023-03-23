class A:
    def __init__(self):
        self.i = 200



class B:
    def __init__(self):
        self.j=20

class C(A,B):#  calll the constructor of all the parent classes. def __init--(self
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

obj=C()
print(obj.i)
print(obj.j)