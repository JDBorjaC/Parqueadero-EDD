from core.parqueadero.vehiculos.Vehiculo import Vehiculo


class Auto(Vehiculo):

    def __init__(self, placa, hasReducedMobility = False):
        super().__init__( placa, hasReducedMobility)