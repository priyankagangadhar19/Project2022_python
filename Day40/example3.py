list1=[1,2,3,4,5]

my_function=lambda list: sum(list)
res= my_function(list1)
print(res)


print ((lambda list: sum(list)) (list1))