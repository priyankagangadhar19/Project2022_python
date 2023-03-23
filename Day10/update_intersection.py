fruits={"apple","mango","grapes","kiwi"}
basket={"apple","banana","kiwi","watermelon"}
new_set=fruits.intersection_update(basket)
print(new_set)



#Example2
fruits={"apple","banana","mango","grapes"}
juice={"apple","sapota","mango","watermelon"}
new_set=fruits.intersection(juice)

print(fruits) #{"apple","banana","mango","grapes"}
print(juice) #{"apple","sapota","mango","watermelon"}
print(new_set) #{'apple', 'mango'}

fruits.intersection_update(juice) #add only common elements to fruits
print(fruits) #{'mango', 'apple'}
print(juice) #{"apple","sapota","mango","watermelon"}
