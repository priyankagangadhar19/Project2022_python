class Vehicle:

    def __init__(self,n):
        self.numer_of_wheels=n


class Bike(Vehicle):

    def __init__(self):
        super().__init__(2)


class Car(Vehicle):

    def __init__(self):
        super().__init__(4)


b1=Bike()
print(b1.numer_of_wheels)

c1=Car()
print(c1.numer_of_wheels)
