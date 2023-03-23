list1=["b","a","b","c","b"]

print(list1)

#reverse
list1.reverse()
print(list1)


#Sorting alphabetical order/ Numbers
list1.sort()
print(list1)

#sorting reverse alphabetical order.
list1.sort(reverse=True)
print(list1)



list1=["python","selenium","API"]

print(list1)

list2=sorted(list1) #sort the content of list1 and store the result in list2 - list1 will not be modified

print(list2)

print(list1)

list3=[7,1,3,0]
list4=sorted(list3,reverse=True)
print(list4)

print(min(list3))
print(max(list3))
print(sum(list3))

