#how to access instance variable through methods
class A:

    def __init__(self):
        self.insta_var=10

    def insta_method(self):
        print(self.insta_var)

    @classmethod
    def class_method(cls,obj1):
        print(obj1.insta_var)

    @staticmethod
    def static_method(obj1):
        print(obj1.insta_var)

a1=A()
a1.insta_method()


A.class_method(a1)
A.static_method(a1)

#address of the oject(object)--> to access the instance method
#class method-->
#static method--> obj o









