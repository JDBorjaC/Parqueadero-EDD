
class Vehiculo():
    def __init__(self, placa, hasReducedMobility = False):
        self.placa = placa
        self.hasReducedMobility = hasReducedMobility
    
    def keyEquals(self, key) -> bool:
        return self.placa == key
        
    def equals(self, otherCar) -> bool:
        return self.placa == otherCar.getPlaca() and self.hasReducedMobility == otherCar.getHasReducedMobility()
    
    def __str__(self):
        return "{ "+f"{self.placa} - {self.hasReducedMobility}"+" }"

    def getPlaca(self):
        return self.placa

    def getHasReducedMobility(self):
        return self.hasReducedMobility
