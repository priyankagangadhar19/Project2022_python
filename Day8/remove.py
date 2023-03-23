a=["b","a","b","c","b"]
a.insert(-1,"z")
print(a)

a=["api","java",'python',"Java"]
print(a)

a.remove("Java")  #delete the specified element based on its value (1st occurance)-Case Sensitive
print(a)

a.remove("lava") # error  not in list

a.__class__