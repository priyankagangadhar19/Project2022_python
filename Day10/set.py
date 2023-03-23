set
# - collection of  data separated by comma with in {}->{1,2,3}
a={1,2,3,3,False,4.5,"bhanu"}
print(a) #set will not allow duplicate
#it doesnot preserves insertion order -> unordered collection
print(type(a))

print(len(a))

print(a[0]) #'set' object is not subscriptable -> we cant use index