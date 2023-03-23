
list1= ['cat','dog','camel','elephant','cow']

# def  animals(n):
#     return n.startswith('c')
#
# def  animals(n):
#     return n[0]=='c'


list2=list(filter(lambda n: n[0]=='c',list1))
print(list2)