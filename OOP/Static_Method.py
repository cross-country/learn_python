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

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        if 'dia' in self.__dict__ and 'h' in self.__dict__:
            self.__dict__['_area'] = self.make_area(self.dia, self.h)


    def getErea(self):
        print(self._area)


a = Cylinder(2, 2)
a.h = 5
a.getErea()

#print(a.make_area(2, 2))