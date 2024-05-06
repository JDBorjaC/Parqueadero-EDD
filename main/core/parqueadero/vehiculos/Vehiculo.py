from core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo


class Vehiculo():
    def __init__(self, placa:str, type, pos):
        self.placa = placa
        self.type = type
        self.pos = pos

    #La "key" del vehiculo es su placa. Útil para saber si ya existe un vehículo con la placa
    def keyEquals(self, key) -> bool:
        return self.placa == key

    #Compara la totalidad del objeto con otra instancia.
    def equals(self, otherVehicle) -> bool:
        if isinstance(otherVehicle, Vehiculo):
            return self.placa == otherVehicle.getPlaca() and self.type == otherVehicle.getPlaca()
        return False
    
    def __str__(self):
        msg = str(self.placa) +", "+ str(self.type)
        return msg

    def getPlaca(self) -> str:
        return self.placa

    def getType(self) -> TipoVehiculo:
        return self.type
    
    def getPos(self) -> str:
        return self.pos
