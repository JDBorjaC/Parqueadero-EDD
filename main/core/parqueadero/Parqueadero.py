from core.listas.ListaEnSimple import LinkedList
from core.parqueadero.pisos.Piso import Piso
from core.parqueadero.pisos.Posicion import Posicion
from core.parqueadero.vehiculos.HoraIngreso import HoraIngreso
from core.parqueadero.vehiculos.Vehiculo import Vehiculo


class Parqueadero():
    def __init__(self):
        self.floors = LinkedList()
        self.vehicles = LinkedList() #Vehiculo(placa, tipo)
        self.horasIngreso = LinkedList() #[placa, horaIngreso]
        for i in range(1, 4):
            self.floors.append(Piso("F" + str(i), 10, 21))

    def getFloor(self, index) -> Piso:
        return self.floors.get(index).data

    def addVehicle(self, floorNumber, positionName, placa, hour) -> bool:
        position = self.getFloor(floorNumber).getSlotByName(positionName)
        vehicle = Vehiculo(placa, position.getType(), "F"+str(floorNumber+1)+positionName)
        if not self.vehicles.containsObject(vehicle):
            position.fillSlot(vehicle)
            self.addVehicleToList(vehicle)
            self.horasIngreso.append(HoraIngreso(vehicle.getPlaca(), hour))
            return True
        return False

    def addVehicleToList(self, vehicle):
        self.vehicles.append(vehicle)

    def removeVehicle(self, floorNumber, positionName, hora_ingreso, hora_salida) -> float:
        position = self.getFloor(floorNumber).getSlotByName(positionName)
        placa = position.getVehicle().getPlaca()
        self.horasIngreso.delete(placa)
        self.vehicles.delete(placa)
        position.clearSlot()
        return self.checkout(placa, hora_ingreso,hora_salida)

    def checkout(self, placa, hora_ingreso, hora_salida) -> float:
        horas = (hora_salida - hora_ingreso).total_seconds()/3600
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

    def getVehiclesInFloor(self, floor):
        searchIn = self.getFloor(floor)
        vehicles = searchIn.getAllVehicles()
        return vehicles