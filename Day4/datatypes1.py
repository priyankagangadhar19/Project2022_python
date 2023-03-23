#identifier-> user given name for variable ,class , function...
# contains a-z A-Z 0-9 _
# Cant start with digit
# case sensitive
#no limit on max length of the name
# no keywords
import keyword
print(keyword.kwlist)
My_import=10

#data type- type of the information stored in a variable
# how do u find the data type of a variable -using type() function
#Number: int float complex
a=10 #int
print(type(a))

a=10.23 #float
print(type(a))

b=2j #comlpex
print(type(b))

#String : str
s="Bhanu" #str -group of character- anything inside quotes
print(type(s))

p="10.23"
print(p)
print(type(p))

q=10
print(q)
print(type(q))
