class Vehicle:
    def start_vehicle (self):
        print("Start the engine")

class Car(Vehicle):
    def start_vehicle(self):
        print("Key start", end=' ')
        

class Bike(Vehicle):
    def start_vehicle(self):
        print("Kick start", end=' ')
        
        




def start_engine(allvehichles): #method overriding- creating our own class
                                    # to fetch overall value or result
    for Vehicle in allvehichles:
        Vehicle.start_vehicle()
        print()


start_engine([Car(),Bike()])




