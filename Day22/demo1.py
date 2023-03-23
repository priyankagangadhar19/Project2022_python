list1=[1,3,5,-7,-9,-3]
# new=[]
#
# for i in list1:
#     if i>=0:
#         new.append(i)
# print(new)

new=[i for i in list1 if i>0 ]
print(new)

new=[i for i in list1 if i<0]
print(new)

