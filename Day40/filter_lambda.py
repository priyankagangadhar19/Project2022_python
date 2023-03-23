# # only positive values
# list1=[0,1,-1,4,5]
#
# def filter_condition(n):
#     if n>0:
#         return True
#     else:
#         return False
#
#
# list2=list(filter(filter_condition,list1))
# print(list2)

list1=[0,1,-1,4,5]
list2=list(filter(lambda n:n>0,list1))
print(list2)
#we are using higher order function> used lambda expression