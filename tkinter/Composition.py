class WinDoor:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, height, width1, width2):
        self.height = height
        self.width = width1
        self.lenght = width2
        self.wd = []
    def __square(self):
        return 2 * self.height * (self.width + self.lenght)

    def addWD(self, h, w):
        self.wd.append(WinDoor(h, w))

    def workSurface(self):
        new_square = self.__square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def getWallSquare(self):
        return self.__square()

    def getWallPapers(self, l, w):
        wpaper = self.workSurface() / (l * w)
        message = 'You need {} rolls of wallpaper'.format(wpaper)
        return message



r1 = Room(6, 3, 2.7)
print(r1.getWallSquare())
r1.addWD(1, 1)
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.workSurface())

print(r1.getWallPapers(10, 0.55))