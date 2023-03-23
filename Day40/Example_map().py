#add hi beffore all the names

all_names=['Kirti','Shruthi','Roopa','Suhas']

def to_names(n):
    return 'Hi ' + n

list2=list(map(to_names,all_names))
print(list2)

#------or----

all_names=list(map(to_names,all_names))
print(all_names)