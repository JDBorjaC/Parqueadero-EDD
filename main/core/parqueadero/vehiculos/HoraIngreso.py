import datetime


class HoraIngreso():

    def __init__(self, placa, hora):
        self.placa = placa
        self.hora = hora

    def keyEquals(self, key) -> bool:
        return self.placa == key

    def getPlaca(self) -> str:
        return self.placa

    def getHora(self) -> datetime:
        return self.hora