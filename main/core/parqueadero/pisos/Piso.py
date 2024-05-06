from main.core.parqueadero.pisos.Posicion import Posicion
from main.core.listas.ListaEnSimple import LinkedList
from main.core.listas.Nodo import Nodo
<<<<<<< Updated upstream
=======
from main.core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo

>>>>>>> Stashed changes

class Piso():
    def __init__(self, name, rows, columns):
        self.name = name
        self.positions = LinkedList()
              
        for i in range(rows):
            for j in range(columns):
                if j < 12:
                    kind = TipoVehiculo.car
                elif j < 20:
                    kind = TipoVehiculo.motorcycle
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