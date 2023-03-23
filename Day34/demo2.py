class Person:

    def __init__(self,name,age=18):
        self.name=name
        self.age=age



class Student(Person):

    def __init__(self,id,name,age=None):
        if age==None:
            Person.__init__(self,name)
        else:
            Person.__init__(self, name,age)
        self.sid=id


p1=Person('Bhanu',16)
print(p1.name,p1.age)

s1=Student(1,'Ravi')
print(s1.sid,s1.name,s1.age)

s2=Student(2,'Shruthi',20)
print(s2.sid,s2.name,s2.age)
