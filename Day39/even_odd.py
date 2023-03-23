list1=[1,2,3,4,5,6,7,8,9,10]

def filter_odd(n):
    if n%2!=0:
        return True
    else:
        return False


list2=list(filter(filter_odd,list1))
print(list2)

# -----------or-------------
list1=[1,2,3,4,5,6,7,8,9,10]

def filter_odd(n):
    return n%2!=0



list2=list(filter(filter_odd,list1))
print(list2)
