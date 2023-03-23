class Emp:

    def __init__(self, new_name, city=None):
        self.name = new_name
        if city == None:
            self.city = 'Bengaluru'
        else:
            self.city = city


e1 = Emp('Arun', 'Agra')
print(e1.name)
print(e1.city)

e2 = Emp('Chandru')
print(e2.name)
e2.name = 'Chandrashekhar'
print(e2.name)
print(e2.city)

e3 = Emp(city='Delhi', new_name='Ravi')
print(e3.name)
print(e3.city)

a=('surya','surath')
e4=Emp(*a)
print(e4.name)
print(e4.city)

print(e4.__dict__)  #internally instance variables are  stored in a dictionary format.

#parametr, argumets, list, tuple, set,dict  all can be done
#packing unpacking,*a