class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        global p3
        p3 = (Person('Alex', 12))
        return p3

p1 = Person('John', 45)
p2 = Person('Sergei', 38)
p4 = Person('Josh', 47)

p1 + p2

print(p3)