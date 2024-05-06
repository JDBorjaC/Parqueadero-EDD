from main.core.parqueadero.vehiculos import Vehiculo
<<<<<<< Updated upstream
from main.core.parqueadero.vehiculos.Auto import Auto
from main.core.parqueadero.vehiculos.Motocicleta import Motocicleta
=======
from main.core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo
>>>>>>> Stashed changes


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

    def validToAdd(self, vehicle):
        return self.type == vehicle.getType()
        
    def fillSlot(self, vehicle) -> None:
        self.vehicle = vehicle
    
    def clearSlot(self):
        self.vehicle = None

    def getVehicle(self) -> Vehiculo:
        return self.vehicle

    def getPuesto(self) -> str:
        return self.puesto

    def getType(self) -> TipoVehiculo:
        return self.kind
    
    def print(self):
        print("Ubicación: "+self.piso.getName()+self.puesto+ "    Tipo: "+ self.kind+"    Cupo: ",not self.vehicle,"    Carro: "+self.vehicleData())

    def vehicleData(self) -> str:
        if self.vehicle:
            return str(self.vehicle)
        else:
            return "None"
