#static method -creating using the decorator @staticmethod
#static method  will not have self or cls as argument
#we access/call the static method directly using class Name
#generally the class which contains static method will not have any instance or class variable

class Utility: #just to store reusable methods-class has No Class variable , has no instance variable

    @staticmethod
    def read_data_from_xl(): #reuse it in many project
        print('reading data from xl')

Utility.read_data_from_xl()