class A:

    def __init__(self):
        self.__num=600           #private

    def getJ(self):
        return self.__num

    def setJ(self,j):
        self.__num=j

a1=A()
print(a1.getJ())
a1.setJ(300)
print(a1.getJ())