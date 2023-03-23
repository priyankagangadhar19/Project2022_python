emp={} #creating empty dict
print(type(emp))
print(len(emp))

emp={"id":"A1","name":"bhanu"}

#how to get the value from dict
v=emp['name']
print(v)

v=emp.get('name')
print(v)

v=emp.get('NAME') #if key is not present it returns 'None'
print(v)

v=emp['NAME'] #if key is not present it returns error
print(v)













