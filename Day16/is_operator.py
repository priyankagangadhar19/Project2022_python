a=[1,2,3]
b=[4,5,6]
c=b

print(a is b)
print(c is b)

#identity operator is-> check if the variable is pointing to same memory are not
list1=[1,2,3]
list2=[4,5,6]
list3=list2

print( list1 is list2) #False
print( list3 is list2) #True

print( list1 is not list2) #True
print( list3 is not list2) #False


listA=[4,5,6]
listB=listA.copy()
print( listB is listA) #False
print( listB is not listA) #True
