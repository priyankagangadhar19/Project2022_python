class A:

    def __init__(self):
        self.a= 10
        self.b = 100

class B(A):
    def __init__(self):
        # A.__init__(self)

        super().__init__()
        self.b = 1000



obj1= A()
print(obj1.a)
print(obj1.b)

obj2=B()
print(obj2.a)
print(obj2.b)
