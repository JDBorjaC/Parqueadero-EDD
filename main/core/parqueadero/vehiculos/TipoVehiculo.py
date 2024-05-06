from enum import Enum
class TipoVehiculo(Enum):
    car = 1
    motorcycle = 2
    reduced_mobility = 3

    def __str__(self):
        return self.name