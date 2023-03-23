#accessing class variable through methods
class A:
    class_var=10

    def instance_method(self):
        print(A.class_var)
        print(self.class_var)

    @classmethod
    def class_method(cls):
        print(A.class_var)
        print(cls.class_var)

    @staticmethod
    def static_method():
        print(A.class_var)

obj1=A()
obj1.instance_method()
A.class_method()
A.static_method()
Shared in
