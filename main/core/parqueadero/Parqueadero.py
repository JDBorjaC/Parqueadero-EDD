from main.core.listas.ListaEnSimple import LinkedList
from main.core.parqueadero.pisos.Piso import Piso
from main.core.parqueadero.pisos.Posicion import Posicion
from main.core.parqueadero.vehiculos.Vehiculo import Vehiculo


class Parqueadero():
    def __init__(self):
        self.floors = LinkedList()
        self.vehicles = LinkedList()
        for i in range(1, 3):
            self.floors.append(Piso("F"+str(i), 21, 10))
        
    def getFloor(self, index) -> Piso:
        return self.floors.get(index).data
    def addVehicle(self, floorNumber, positionName, vehicle, hour) -> bool:
        if not self.vehicles.containsObject(vehicle):
            position = self.getFloor(floorNumber).getSlotByName(positionName)
            if position.validToAdd(vehicle):
                position.fillSlot(vehicle, hour)
                self.vehicles.append(vehicle)
                return True
        return False
    
    def removeVehicle(self, position, hour) -> bool:
        position.clearSlot(hour)

    def getVehicle(self, placa) -> Vehiculo:
        return self.vehicles.getBy(placa).data

    def getPosition(self, nombre) -> Posicion:
        # Ejemplo de nombre: F1A4
        piso = self.floors.getBy(nombre[:2]).data
        if piso:
            piso.getSlotByName(nombre[2:4])