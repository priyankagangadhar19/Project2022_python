class Emp:
    comp='TCS'

    def __init__(self,name):
        self.name=name

print(Emp.__dict__)
#how to access instance variable?--> using the object
e1=Emp('Bhanu')
print(e1.__dict__)

#how to access class variable?--> using class name or using instance
print(Emp.comp)
print(e1.comp)

e2=Emp('Ravi')
e2.name='Ravi Surya'

print(e1.name)#Bhanu
print(e2.name)#Ravi Surya

Emp.comp='ABB'
print(Emp.comp)
print(e1.comp)
print(e2.comp)
