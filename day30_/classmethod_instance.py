class Emp:
    comp='TCS'

    def __init__(self,name):
        self.name=name

    def print_emp1(self):
        print(self.name)

Emp.print_emp1() #print_emp1 is an instance  method

# error because we cannot access class method/variable using instance method/variable
# we can access class variable using class method









