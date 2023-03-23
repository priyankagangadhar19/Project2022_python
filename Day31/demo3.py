#how to create instance variable & how to access it
class A:

    def __init__(self):
        self.insta_var=10

obj1=A()
print(obj1.insta_var)

#we cant access instance variable using class name