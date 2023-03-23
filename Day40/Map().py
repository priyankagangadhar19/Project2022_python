list1=[1,2,3,4]

def map_condition(n):
    return n+1


list2=list(map(map_condition,list1))

print(list2)
