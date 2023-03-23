class Emp:
    comp='TCS'

    def __init__(self,name):
        self.name=name

    def print_emp1(self): #instance method- takes self as 1st arg
        print(self.name)
        print(Emp.comp)
        print(self.comp)

    @classmethod #@ is called as decorator(indicates the class method
    def print_emp2(cls): #class method- takes cls as 1st arg
        print(Emp.comp)
        print(cls.comp)
#using class name we can access only -> class variable and class methods
#using object we can access-> instance varibale , instance method, class variable,class methods

e1=Emp('Bhanu')
e1.print_emp1()

Emp.print_emp2()
e1.print_emp2()