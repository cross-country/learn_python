import random as rd

class Unit:
    def __init__(self, id_number, belongs):
        self.id = id_number
        self.command = belongs


class Heroes(Unit):
    def __init__(self, id_number, belongs, name):
        Unit.__init__(self, id_number, belongs)
        self.name = name
    level = 1

    def level_increase(self):
        self.level += 1


class Soldier(Unit):
    def follow_hero(self, hero):
        print('I follow my lord {}'.format(hero))


Thorin = Heroes(1, 'dwarves', 'Thorin')
Pale_Ork = Heroes(2, 'orcs', 'Azog')

count1 = 3
count2 = 30
orcs_list, dwarves_list = [], []
for i in range(50):
    number = rd.randint(0, 100)
    if number < 50:
        tvar = Soldier(count2, 'orcs')
        orcs_list.append(tvar)
        count2 += 1
    else:
        tvar = Soldier(count1, 'dwarves')
        dwarves_list.append(tvar)
        count1 += 1

print('there are {} orcs in first army and '.format(len(orcs_list)), '\n',
      'there are {} dwarves in second army'.format(len(dwarves_list)))

if len(orcs_list) < len(dwarves_list):
    Thorin.level_increase()
elif len(orcs_list) > len(dwarves_list):
    Pale_Ork.level_increase()

dwarves_list[9].follow_hero(Thorin.name)
print(Thorin.id, '\n', dwarves_list[9].id)

orcs_list[11].follow_hero((Pale_Ork.name))
print(Pale_Ork.id, '\n', orcs_list[11].id)

print('Level of Thorin is {} '.format(Thorin.level), 'Level of Azog is {}'.format(Pale_Ork.level))
