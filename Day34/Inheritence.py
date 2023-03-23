class A:
    a=10

    def __init__(self):
        self.b=20


    @classmethod
    def class_method(cls):
        print(cls.a)


    def instace_method(self):
        print(self.b)

class B(A):
    pass

print(B.a)
B.class_method()
obj=B()
print(obj.b)
obj.instace_method()
