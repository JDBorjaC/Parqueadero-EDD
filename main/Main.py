from main.core.parqueadero.pisos.Piso import Piso
from main.core.parqueadero.Parqueadero import Parqueadero
from main.core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo
from main.core.parqueadero.vehiculos.Vehiculo import Vehiculo

parqueadero = Parqueadero()

parqueadero.addVehicle(0, "A2", Vehiculo("MXN569", TipoVehiculo.car), "ALGUNAHORAAHÍ")

parqueadero.getFloor(0).getSlotByName("A2").print()