from core.parqueadero.vehiculos.Vehiculo import Vehiculo

class Motocicleta(Vehiculo):

    def __init__(self, placa, hasReducedMobility = False):
        super().__init__(placa, hasReducedMobility)