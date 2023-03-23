class Animal:
    def make_sound(self):
        print("Sound of the animals will be diff")

class Cat(Animal):
    def make_sound(self):
        print("Meow",end=' ')

class Dog(Animal):
    def make_sound(self):
        print("Bow",end=' ') #to print ext to each other




def make_sound_of_animals(animals): #method overriding- creating our own class
                                    # to fetch overall value or result
    for animal in animals:
        animal.make_sound()
    print()  #next line


make_sound_of_animals([Cat(),Cat()])
make_sound_of_animals([Dog(),Dog()])
make_sound_of_animals([Dog(),Cat()])

