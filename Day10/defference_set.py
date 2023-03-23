fruits={"apple","banana","mango","grapes"}
juice={"apple","sapota","mango","watermelon"}
icecreams={"strawberry","mango","apple"}
new_set=fruits.difference(juice) #create new set and add  elements present in only fruits
print(new_set)
new_set=juice.difference(fruits) #create new set and add elements present only in juice
print(new_set)

result=juice.issubset(fruits) #all the elements of juice are present in fruits
print(result)
result=icecreams.issubset(fruits) #all the elements of icecream are not present in fruits
print(result)

result=fruits.issuperset(juice) #fruits contains all the elements of juice
print(result)

result=fruits.issuperset(icecreams)#fruits does not contains all the elements of juice
print(result)

#Example2
fruits={"apple","banana","mango","grapes"}
juice={"apple","mango"}
icecream={"mango","strawberry"}

result=juice.issubset(fruits) #all the elements of juice are present in fruits
print(result) #True

result=icecream.issubset(fruits) #all the elements of icecream are not present in fruits
print(result) #False

result=fruits.issuperset(juice) #fruits contains all the elements of juice
print(result) #True

result=fruits.issuperset(icecream)#fruits does not contains all the elements of juice
print(result) #False


#Example3

fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set1=fruits.difference_update(basket)
print(new_set)

new_set1=basket.difference_update(fruits)
print(new_set)