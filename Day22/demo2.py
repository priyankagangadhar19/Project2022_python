#list  comprehension
list1=['apple juice','apple milkshake','banana milkshake']
new=[]

for i in list1:
    if 'milkshake' in i:
        new.append(i)
print(new)

new=[i for i in list1 if 'milkshake' in i]
print(new)