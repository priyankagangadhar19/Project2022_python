a={"java","python","c#","selenium","api"}
print(a)

a.remove("c#")
print(a)

a.discard("api")
print(a)

a.discard("QTP")
print(a)

a.clear() #delete all elements from the set
print(a)

a.remove("QTP") #u can not remove non existing element ->KeyError: 'QTP'

a.pop()
print(a)