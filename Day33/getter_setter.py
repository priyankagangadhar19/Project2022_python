#Simple example for encapsulation- hide the data (private) give indirect access through getters (read) and setters (write) method
class A:

    def __init__(self):
        self.__j=100            #private

    def getJ(self):
        return self.__j

    def setJ(self,j):
        self.__j=j

a1=A()
print(a1.getJ())
a1.setJ(10)
print(a1.getJ())










