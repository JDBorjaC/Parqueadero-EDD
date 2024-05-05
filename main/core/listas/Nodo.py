class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data
