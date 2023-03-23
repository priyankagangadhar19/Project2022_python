fruits={"apple","banana","mango","grapes"}
juice={"apple","sapota","mango","watermelon"}
icecreams={"strawberry","mango","apple"}
candy={"orange","chocolate"}
print(candy.isdisjoint(fruits))


print(candy.isdisjoint(juice))

print(candy.isdisjoint(fruits))
print(candy.isdisjoint(icecreams))

print(juice.isdisjoint(fruits))

print(icecreams.isdisjoint(fruits))

#example2

fruits={"apple","banana","mango","grapes"}
juice={"apple","mango"}
icecream={"mango","strawberry"}
candy={"orange","chocolate"}
print(candy.isdisjoint(fruits)) #everything is not common ? yes True #2 set are completely diff
print(juice.isdisjoint(fruits)) #everything is not common ? No Fasle
print(icecream.isdisjoint(fruits))#everything is not common ?No Fasle