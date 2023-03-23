emp1={"id":"A1","name":"bhanu"}

emp1['name']='Ravi' #key already present so it will change the value
print(emp1)

emp1['city']='Pune' #key is not present so it will add key+value
print(emp1)

emp1={"id":"A1","name":"bhanu"}
emp1.setdefault('name','Ravi') #key already present so dont change the value
print(emp1)

emp1.setdefault('city','Pune') #key not present so add key+value
print(emp1)