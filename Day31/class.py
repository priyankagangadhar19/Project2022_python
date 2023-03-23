class A:
    """This is my class A"""

    class_var:str ='class var'

    def __init__(self):
        self.insta_var="insta_var"

    def insta_method(self,new_val:str):
        self.insta_var=new_val

    @classmethod
    def class_method(cls):
        print(cls.class_var)

    @staticmethod
    def static_method():
        print('This is static method')
