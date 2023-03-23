list1= ['cat','dog','tiger','elephant','rat']

def  animals(n):
    return  len(n)<=3

list2=list(filter(animals,list1))
print(list2)




list1= ['cat','dog','camel','elephant','cow']

def  animals(n):
    return n.startswith('c')

def  animals(n):
    return n[0]=='c'


list2=list(filter(animals,list1))
print(list2)

