#print the content of dict using for loop
a={"name":"bhanu","sub":"Python","duration":50}

for key in a.keys():
    print(key)
else:
    print('-----')

for value in a.values():
    print(value)
else:
    print('-----')

for key in a:
    value = a.get(key)
    print(key,'-',value)
else:
    print('-----')