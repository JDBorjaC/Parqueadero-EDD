class Posicion():

    #puesto -> "A1", fila A, pos 1
    #kind -> [0, 2], moto, carro, disc

    def __init__(self, puesto, kind, has):
        self.puesto = puesto
        self.kind = kind
        self.has = has
    
    def fillSlot(self, vehicle):
        self.has = vehicle
    
    def printData(self):
        print("Ubicación: ",self.puesto, "    Tipo: ", self.kind, "    Cupo: ", not self.has)
    
