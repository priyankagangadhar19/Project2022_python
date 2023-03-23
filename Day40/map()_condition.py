#all the name should be added to new list as upper case
list1=['Arun','Bhanu','Chandana','DEEPA']
list2=[]

# for name in list1:
#     uname=name.upper()
#     list2.append(uname)
#
# print(list2)

def to_upper(name):
    return name.upper()

list2=list(map(to_upper,list1))
print(list2)