import Posicion

class Piso():

    def __init__(self, name):
        self.name = name
        #pos(pos, type, filled)
        self.positions = []

        for i in "ABCDEFGHIJ":
            for j in range(21):
                if(j < 12): 
                    kind = 0
                elif(j<20):
                    kind = 1
                else:
                    kind = 3
                self.positions.append(Posicion(i+j, kind, False))

    def printPositions(self):
        for i in range(210):
            print(self.positions[i].printData)