from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    def __init__(self, diameter, height):
        self.dia = diameter
        self.h = height
        self.__area = self.make_area(self.dia, self.h)

    def __setattr__(self, attr, value):
        #self.__area = self.make_area(self.dia, self.h)
        self.__dict__[attr] = value

    def getErea(self):
        print(self.__area)


a = Cylinder(2, 2)
a.h = 5
print(a.h)
a.getErea()

#print(a.make_area(2, 2))