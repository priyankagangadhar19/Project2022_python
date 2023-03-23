class Emp:
    comp='TCS'


e1=Emp()
e2=Emp()

# print(Emp.comp)
print(e1.comp)
print(e2.comp)

Emp.comp='ABB'

print(Emp.comp)
print(e1.comp)
print(e2.comp)

e1.comp='ITC'
print(Emp.comp)
print(e1.comp)
print(e2.comp)