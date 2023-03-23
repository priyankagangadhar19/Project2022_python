# print max / greatest number from list using for loop.
list1=[1,5,2,7,8,3]
max=0

for n in list1:
    if n>max:
        max=n
print(max)

#if it contains negative number

list1=[1,-5,-2,-7,-8,-3]
max=list1[0]

for n in list1:
    if n>max:
        max=n
print(max)