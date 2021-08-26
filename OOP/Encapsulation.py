class Vehicle:
    def __init__(self, model, eng, color):
        self.model = model
        self.__engine_volume = eng
        self.__color = color
        self.__horse_power = 25

    def __hp(self):
        return  self.__engine_volume * 100

    def setEngineVolume(self, vol):
        self.__engine_volume = vol

    def setColor(self, color):
        self.__color = color

    def getEngineVolume(self):
        return self.__engine_volume

    def getColor(self):
        return self.__color

    def getHorsepower(self):
        return self.__hp()


Car = Vehicle('BMW', 1.8, 'red')
print(Car.getColor())
print(Car.getHorsepower())
#print(Car.getColor())
