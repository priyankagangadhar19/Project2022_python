#can a method take both self and cls ?-No
#a method should be either instance method or class method (not both)
# class Emp:
#     comp = 'TCS'
#
#     def test(self, cls):
#         self.name = 'bhanu'
#         cls.comp = 'ABB'
#
# e1 = Emp()
# e1.test()



#how to explicitly indicate that the method is class method?
#using the decorator ->@classmethod
#is it mandatory to use @classmethod?-No
class Emp:
    comp = 'TCS'

    def __init__(self):
        self.name = 'bhanu'

    def test1(self):
        print(self.name)

    def test2(cls):
        print(cls.comp)

    @classmethod
    def test3(cls):
        print(cls.comp)

e1 = Emp()
e1.test1()
e1.test2()
e1.test3()