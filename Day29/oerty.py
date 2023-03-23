class Emp:
    def __init__(self,eid,name,city,email):
        self.eid = eid
        self.name = name
        self.city = city
        self.email = email

    def print_emp_details(self):
        print(self.eid)
        print(self.name)
        print(self.city)
        print(self.email)


e1=Emp('A1','Arun','Agra','arun@gmail.com')
e1.print_emp_details()
        # print(e1.eid)
        # print(e1.name)
        # print(e1.city)
        # print(e1.email)

e2=Emp('A2','Asha','Ahmadabad','asha@gmail.com')
e2.print_emp_details()
