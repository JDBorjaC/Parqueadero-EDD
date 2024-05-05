from main.core.parqueadero.vehiculos import Vehiculo
from main.core.parqueadero.vehiculos.Auto import Auto
from main.core.parqueadero.vehiculos.Motocicleta import Motocicleta


class Posicion():

    #puesto -> "A1", fila A, pos 1
    #kind -> ["car", "motorcycle", "reduced_mobility"]

    def __init__(self, piso, puesto, kind, vehicle):
        self.piso = piso
        self.puesto = puesto
        self.kind = kind
        self.vehicle = vehicle
        self.lastTimeFilled = None
        
    def keyEquals(self, key):
        return self.puesto == key

    def validToAdd(self, vehicle):
        if self.kind == "reduced_mobility":
            return vehicle.hasReducedMobility
        return (self.kind == "car" and isinstance(vehicle, Auto)) or (self.kind == "motorcycle" and isinstance(vehicle, Motocicleta))
        
    def fillSlot(self, vehicle, hour) -> None:
        self.vehicle = vehicle
        self.lastTimeFilled = hour
    
    def clearSlot(self, hora_salida):
        self.vehicle = None
        # TODO: Manejar el cobro del parqueo (por el momento existe el método precioSosio)

    def precioSosio(self, hora_salida):
        horas = (hora_salida - self.vehicle.lastTimeFilled)/3600
        if horas % 1 > 0:
            return 2000*(1 + int(horas))
        return 2000*int(horas)

    def getVehicle(self) -> Vehiculo:
        return self.vehicle

    def getPuesto(self) -> str:
        return self.puesto

    def getKind(self) -> str:
        return self.kind
    
    def print(self):
        print("Ubicación: "+self.piso.getName()+self.puesto+ "    Tipo: "+ self.kind+"    Cupo: ",not self.vehicle,"    Carro: "+self.vehicleData())

    def vehicleData(self) -> str:
        if self.vehicle:
            return str(self.vehicle)
        else:
            return "None"
