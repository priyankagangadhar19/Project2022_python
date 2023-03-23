#give example for encapsulation
class A:
    a=10            #public class var
    __b=20          #private class var

    def __init__(self):
        self.x=30       #public instance var
        self.__y=40     #private intance var

    @classmethod
    def printa(cls):       #public class method
        print(cls.a)

    @classmethod
    def __printb(cls):      #private class method
        print((cls.__b))

    def printx(self):       #public intance method
        print(self.x)

    def __printy(self):     #print instance method
        print(self.__y)


obj1=A()
print(A.a)
# print(A.__b)  # we cant access private class variables

print(obj1.x)
# print(obj1.__y) # we cant access private instace variables

A.printa()
# A.__printb()  # we cant access private class methods

obj1.printx()

# obj1.__printy() # we cant access private instance methods
