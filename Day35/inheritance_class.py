class A:
    i=10

    def __init__(self):
        self.j=20

    def testA(self):
        print('instance method of class A')
        print(self.j)

    @classmethod
    def testB(cls):
        print('class method of class A')
        print(cls.i)

    @staticmethod
    def testC():
        print('static method of class A')

obj=A()
obj.testA()

A.testB()

A.testC()










