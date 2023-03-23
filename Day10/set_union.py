fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set=fruits.union(basket)
print(new_set)

#union() its is a method used in set to combine the common elements from different sets and create a new set

a={1,10,20,30}
b={2,4,20,30}
a.update(b)
print(a)

fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set=fruits.intersection(basket)
print(new_set)

fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set=fruits.difference(basket)
print(new_set)

fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set=basket.difference(fruits)
print(new_set)

#example2
fruits={"apple","banana","mango","grapes"}
juice={"apple","sapota","mango","watermelon"}
new_set=fruits.difference(juice) #create new set and add  elements present in only fruits
print(new_set) #b g

new_set=juice.difference(fruits) #create new set and add elements present only in juice
print(new_set) #s w