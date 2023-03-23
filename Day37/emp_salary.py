class Employee:

    def __init__(self,id,name,bill,days):
        self.id= id
        self.name= name
        self.bill= bill
        self.days= days

    def get_salary(self):
        print("Depends on your role")



class Eng(Employee):

    def __init__(self,id,name,bill,days):
        super().__init__(id,name,bill,days)




    def get_salary(Employee, self=None):
        salary= (self.bill) * (self.days)
        print("Your salary is:", salary)

class Manager(Employee):

    def __init__(self, id, name, bill, day):
        super().__init__(id, name, bill, day)

    def salary(Employee, self=None):
        salary = (self.billing) * (self.day) * 100
        print("Your salary is:", salary)

class Employee:

    def __init__(self,id,name,billing,days):
        self.id=id
        self.name=name
        self.billing=billing
        self.days=days


    def get_salary(self):
        print("Your salaray depends on your role")


# class Eng(Employee):
#
#     def __init__(self, id, name, billing, days):
#         super().__init__(id, name, billing, days)
#
#     def get_salary(self):
#         salary=self.billing * self.days
#         print("Dear",self.name,"Your Salary is:",salary)
#
# class Manager(Employee):
#
#     def __init__(self, id, name, billing, days):
#         super().__init__(id, name, billing, days)
#
#     def get_salary(self):
#         salary=(self.billing+100) * self.days
#         print("Dear",self.name,"Your Salary is:",salary)
#
#
#
# def get_salary_for_all(allemployees):
#     for emp in allemployees:
#         emp.get_salary()
#
# e1=Eng(1,'Bhanu',100,20)
# m1=Manager(2,'Sandeep',100,20)
#
# get_salary_for_all([e1,m1])
