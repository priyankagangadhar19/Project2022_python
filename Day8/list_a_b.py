list1=["chocos","icecream","pizza"]

list2=list1
list2[2]="Burger"
print(list2)
print(list2)

list1.insert(2,"Test")
print(list1)

#copy() method

print(list1)
list2=list1.copy()
list2[2]="Idly"

print(list2)