#list -> its a collection of data
a=[1,2,3]  #homogeneous
print(a)
print(type(a))

b=[1,'a',True] #heterogeneous
print(b) #it preserves insertion order - ordered collection

#sequential data type - supports index (subscript)
print(b[0],b[1],b[2])

c=[]   #empty list
print(type(c))

#to find the number of elements present in the list we can use len() ->length  size
print(len(a))
print(len(b))
print(len(c))

#list will allow duplicate
d=[1,2,2]
print(d)
d[0]=7  # we can change the value of list - mutable
print(d)

#new set
a=["priya","abc","xyz"]
print(type(a))
a[2]="hello"
print(a)

