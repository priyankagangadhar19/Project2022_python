class Shape:

    def __init__(self,x,y):
        self.x=x
        self.y=y

class Rectangle(Shape):

    def __init__(self,x,y,h,w):
        super().__init__(x,y)
        self.h=h
        self.w=w
        self.sides=4

class Square(Rectangle):

    def __init__(self,x,y,h):
        super().__init__(x,y,h,h)

r1=Rectangle(10,20,400,800)
print(r1.__dict__)

s1=Square(15,30,500)
print(s1.__dict__)