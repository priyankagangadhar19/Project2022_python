# parent class Bike child class Bullet

class Bike:

    def __init__(self, cc, seats):
        self.wheels = 2
        self.enginecc = cc
        self.seats = seats


class Bullet(Bike):

    def __init__(self):
        Bike.__init__(self, 350, 2)
        self.price = 1.66
        self.sound = 'gudu gudu'
