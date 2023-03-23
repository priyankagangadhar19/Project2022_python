# what are the diff ways to create object of a class
class A:

    def __init__(self):
        self.insta_var = 10

a1 = A()  # by directly calling constructor
print(a1.insta_var)

class B:

    @classmethod  # factory method
    def create_object(cls):
        obj1 = B()
        return obj1


b1 = B.create_object()

class C:

    @staticmethod  # factory method
    def create_object():
        obj1 = C()
        return obj1

c1 = C.create_object()