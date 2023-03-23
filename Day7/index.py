
list1=["b","a","b","c","b"]
indexOf1stb=list1.index("b")
print(indexOf1stb) #0
indexof2ndb=list1.index("b",indexOf1stb+1)
print(indexof2ndb) #2


#code optimization

list1=["b","a","b","c","b"]

print(list1.index("b",list1.index("b")+1)) #2

#To check if the element is present in the list or not
list1=["python","selenium","API","API"]

#print(list1.index("API")) #2
#print("API" in list1) #api is present in list1? yes -> True

#print("BDD" in list1) #BDD is present in list1? no-> False

#print(list1.index("BDD")) #err

print(list1.index("API"))




