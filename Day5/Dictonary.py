a=[1,"bhanu",True] #mutable - we can modify
print(type(a))

b=(1,"bhanu",True,True) #immutable - we cant modify
print(type(b))
print(b)

c={1,"2",3,3} #mutable
print(type(c))

d=frozenset(c)#immutable
print(type(d))


e={"API":"Chandra","Automation":"Bhanu","MT":"Vinay"} #mutable
print(e["API"])
print(type(e))





