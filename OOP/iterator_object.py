import random
class RandomList:
    def __init__(self, quantity=5):
        self.quantity = quantity
        self.random_list = self.generate_list()
    def generate_list(self):
        temp_list = []
        for i in range(0, self.quantity):
            temp_list.append(random.randint(0, 50))
        return temp_list
    def __iter__(self):
        return self
    def __next__(self):
        if self.random_list == []:
            raise StopIteration
        a = self.random_list[0]
        del self.random_list[0]
        return a

a = RandomList(9)
for i in a:
    print(i)
