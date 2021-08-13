import time
import random as rd
def message(name, health):
    msg = '{0} получает сокрушительный удар! У него остается {1} единиц прочности.'
    print(msg.format(name, health))

def final_message(name1, name2):
    msg = '\n{0} повержен! {1} победил!!! Его родные и близкие ликуют.\n Но {0} был достойным противником. '
    print(msg.format(name1, name2))

def battle():
    fight = True
    while fight:
        turn = rd.randint(1, 10)
        if turn > 5:
            Megatron.set_hp(Megatron.health - 20)
            message('MEGATRON', Megatron.health)
            if Megatron.health <= 0:
                time.sleep(2)
                final_message('MEGATRON', 'OPTIMUS PRIME')
                fight = False
        else:
            Optimus_Prime.set_hp(Optimus_Prime.health - 20)
            message('OPTIMUS PRIME', Optimus_Prime.health)
            if Optimus_Prime.health <= 0:
                time.sleep(2)
                final_message('OPTIMUS PRIME', 'MEGATRON')
                fight = False
        time.sleep(4)

class Warrior():
    health = 15
    def set_hp(self, number):
        self.health = number


Optimus_Prime = Warrior()
Optimus_Prime.set_hp(100)

Megatron = Warrior()
Megatron.set_hp(100)

battle()


