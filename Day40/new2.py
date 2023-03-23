#add only odd number to list2
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(filter(lambda n:n%2==1,list1))
print(list2)

list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(filter(lambda n:n%2==0,list1))
print(list2)




#convert km to m

list1=[2,5,9]
def to_meter(n):
    return n * 2.54

list2=list(map(to_meter,list1))
print(list2)