emp={"id":"A1","name":"bhanu"}
print(emp)

#How to change the value
emp['id']="A2"
print(emp)

emp['city']="Bng" #if key does not exists it creates it and stores the value
print(emp)

emp.update({"id":"A3","name":"RAVI","area":"JP Nagar"}) #update/change multiple key-values
print(emp)