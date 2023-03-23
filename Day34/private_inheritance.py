class A:
    __a=10

    def __init__(self):
        self.__b=20


    @classmethod
    def class_method(cls):
        print(cls.__a)


    def instace_method(self):
        print(self.__b)

class B(A):
    pass

A.class_method()
obj=A()
obj.instace_method()
B.class_method()
