class Emp:

    def __init__(self):
        print('i am inside init function of Emp class')
        self.name = 'Bhanu'

e1 = Emp()

e2 = Emp()
e2.name = 'Ravi'

print(e1.name)
print(e2.name)

#name is called as instance variable
