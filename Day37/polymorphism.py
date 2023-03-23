class Shape:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def find_area(self):
        print("Area is a amount of space occupied by the respective shape")



class Rectangle(Shape):

    def __init__(self,x,y,l,w):
        super().__init__(x,y)
        self.l=l
        self.w=w

    def find_area(self):
        area=self.l * self.w
        return area


class Circle(Shape):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def find_area(self):
        area=3.14 * self.r * self.r
        return area

#---------------------------------------------------
def find_the_area(allshapes):
    for shape in allshapes:
        print(shape.find_area())


r=Rectangle(10,15,100,200)
c=Circle(10,15,50)
allshapes=[r,c]
find_the_area(allshapes)
