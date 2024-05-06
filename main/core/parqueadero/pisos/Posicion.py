from core.parqueadero.vehiculos import Vehiculo
from core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo


class Posicion():

    #puesto -> "A1", fila A, pos 1
    #kind -> TipoVehiculo.car/motorcycle/reduced_mobility

    def __init__(self, piso, puesto, type, vehicle):
        self.piso = piso
        self.puesto = puesto
        self.type = type
        self.vehicle = vehicle

    #La "key" es el puesto
    def keyEquals(self, key):
        return self.puesto == key
        
    def fillSlot(self, vehicle) -> None:
        self.vehicle = vehicle
    
    def clearSlot(self):
        self.vehicle = None

    def getVehicle(self) -> Vehiculo:
        return self.vehicle

    def getEstado(self) -> str:
        if self.vehicle:
            return 'Ocupado'
        return 'Libre'

    def getName(self) -> str:
        return self.piso.getName()+self.getPuesto()

    def getPuesto(self) -> str:
        return self.puesto

    def getType(self) -> TipoVehiculo:
        return self.type
    
    def print(self):
        print("Ubicación: "+self.piso.getName()+self.puesto+ "    Tipo: "+ str(self.type)+"    Cupo: ",not self.vehicle,"    Carro: "+self.vehicleData())

    def vehicleData(self) -> str:
        if self.vehicle:
            return str(self.vehicle)
        else:
            return "None"
