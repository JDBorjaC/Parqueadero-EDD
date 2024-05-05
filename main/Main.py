from core.parqueadero.pisos.Piso import Piso
from main.core.parqueadero.Parqueadero import Parqueadero
from main.core.parqueadero.vehiculos.Auto import Auto

parqueadero = Parqueadero()

parqueadero.addVehicle(0, "A2", Auto("MXN569", False), "ALGUNAHORAAHÍ")

parqueadero.getFloor(0).getSlotByName("A2").print()