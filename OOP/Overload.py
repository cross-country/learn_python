class Snow:
    def __init__(self, quantity):
        self.snowflakes = quantity

    def __call__(self, qwty):
        self.snowflakes = qwty

    def __add__(self, other):
        self.snowflakes += other
        return self.snowflakes

    def __sub__(self, other):
        self.snowflakes -= other
        return self.snowflakes

    def __mul__(self, other):
        self.snowflakes *= other
        return self.snowflakes

    def __truediv__(self, other):
        self.snowflakes = round(self.snowflakes / other)
        return self.snowflakes

    def makeSnow(self, row):
        rows = self.snowflakes // row
        last = self.snowflakes % row
        for i in range(rows):
            print('*' * row)
        print('*' * last)


p1 = Snow(5)
p1(200)
p1 / 2
p1.makeSnow(10)