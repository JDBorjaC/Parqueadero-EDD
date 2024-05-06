from core.parqueadero.pisos.Posicion import Posicion
from core.listas.ListaEnSimple import LinkedList
from core.listas.Nodo import Nodo
from core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo

class Piso():
    def __init__(self, name, rows, columns):
        self.name = name
        self.positions = LinkedList()
              
        for i in range(rows):
            for j in range(columns):
                if j < 12:
                    kind = TipoVehiculo.motorcycle
                elif j < 20:
                    kind = TipoVehiculo.car
                else:
                    kind = TipoVehiculo.reduced_mobility
                self.positions.append(Posicion(self, chr(65+i) + str(j+1), kind, False))
    
    def keyEquals(self, key) -> bool:
        return self.name == key

    def getSlotByName(self, name) -> Posicion:
        return self.positions.getBy(name).data

    def getName(self) -> str:
        return self.name

    def printPositions(self):
        for i in range(self.positions.size()):
            self.positions.get(i).data.print()
    
    def getAllVehicles(self):
        vehicles = []
        for i in range(self.positions.size()):
            #Si hay un vehiculo en el slot de indice i,
            if self.positions.get(i).data.getVehicle():
                vehicles.append(self.positions.get(i).data.getVehicle())
        return vehicles
            
            