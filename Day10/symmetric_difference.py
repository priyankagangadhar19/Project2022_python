fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set=fruits.symmetric_difference(basket)
print(new_set)

new_set=basket.symmetric_difference(fruits)
print(new_set)

new_set=fruits.symmetric_difference_update(basket)
print(new_set)

#exaple3

fruits={"apple","banana","mango","grapes"}
juice={"apple","sapota","mango","watermelon"}
new_set=fruits.symmetric_difference(juice) #create new set and add  elements present in only fruits & only in juice
print(fruits)
print(juice)
print(new_set) #b g s w

fruits.symmetric_difference_update(juice) #same as above, but no new set, existing set is modified
print(fruits) #b g s w
print(juice)
