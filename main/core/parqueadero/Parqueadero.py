from main.core.listas.ListaEnSimple import LinkedList
from main.core.parqueadero.pisos.Piso import Piso
from main.core.parqueadero.pisos.Posicion import Posicion
from main.core.parqueadero.vehiculos.HoraIngreso import HoraIngreso
from main.core.parqueadero.vehiculos.Vehiculo import Vehiculo


class Parqueadero():
    def __init__(self):
        self.floors = LinkedList()
        self.vehicles = LinkedList() #Vehiculo(placa, tipo)
        self.horasIngreso = LinkedList() #[placa, horaIngreso]
        for i in range(1, 3):
            self.floors.append(Piso("F" + str(i), 10, 21))

    def getFloor(self, index) -> Piso:
        return self.floors.get(index).data

    def addVehicle(self, floorNumber, positionName, vehicle, hour) -> bool:
        if not self.vehicles.containsObject(vehicle):
            position = self.getFloor(floorNumber).getSlotByName(positionName)
            if position.validToAdd(vehicle):
                position.fillSlot(vehicle)
                self.vehicles.append(vehicle)
                self.horasIngreso.append(HoraIngreso(vehicle.getPlaca(), hour))
                return True
        return False

    def removeVehicle(self, position, hora_salida) -> bool:
        self.horasIngreso.delete(position.getVehicle().getPlaca())
        self.vehicles.delete(position.getVehicle())
        position.clearSlot()
        #TODO: proceder al checkout de la vainola (por ahora existe el método pagaCole())

    def pagaCole(self, placa, hora_salida) -> float:
        hora_ingreso = self.horasIngreso.getBy(placa).data.getHora()
        horas = (hora_salida - hora_ingreso)/3600
        if horas % 1 > 0:
            return 2000*(1 + int(horas))
        return 2000*int(horas)

    def getVehicle(self, placa) -> Vehiculo:
        return self.vehicles.getBy(placa).data

    def getPosition(self, nombre) -> Posicion:
        # Ejemplo de nombre: F1A4
        piso = self.floors.getBy(nombre[:2]).data
        if piso:
            return piso.getSlotByName(nombre[2:4])
        return None