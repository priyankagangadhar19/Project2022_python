#removing from dict
emp1={"id":"A1","name":"bhanu"}
emp2=emp1

emp2['name']='Ravi'

print(emp1)
print(emp2)

emp1={"id":"A1","name":"bhanu"}
emp2=emp1.copy()

emp2['name']='Ravi'

print(emp1)
print(emp2)