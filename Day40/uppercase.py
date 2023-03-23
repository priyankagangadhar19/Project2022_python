list1=['Arun','Banhu','Chandu','Deepa']

list2=list(map(lambda n:n.upper(),list1))
print(list2)


#add only names which starts with c
list1=['cat','cow','tiger','elephant','camel']
list2=list(filter(lambda n:n.startswith('c'),list1))
print(list2)




