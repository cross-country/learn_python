from random import *

class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forget(self):
        index = randint(0, len(self.knowledge))
        self.knowledge.pop(index)


alex = Teacher()
andrew = Pupil()
sergei = Pupil()
data1 = Data('math', 'algebra', 'geometry', 'literature', 'foreign language', 'chemistry')

alex.teach(data1[0], andrew, sergei)
andrew.take(data1[1])
andrew.take(data1[2])
andrew.take(data1[3])
print(sergei.knowledge, '\n', andrew.knowledge)
andrew.forget()
print(andrew.knowledge)