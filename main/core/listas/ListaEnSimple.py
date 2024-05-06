from .Nodo import Nodo

class LinkedList:
    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def addFirst(self, data):
        self.head = Nodo(data, self.head)

    # Método para verificar si la estructura de datos esta vacia
    def isEmpty(self):
        return self.head == None

    # Método para agregar elementos al final de la lista enlazada
    def append(self, data):
        #Si la lista no existe, entonces se crea
        if not self.head:
            self.head = Nodo(data)
            return
        #recorre toda la lista hasta llegar al final
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        #Cuando llega al final de la lista, enlaza el último nodo con
        #el nuevo nodo que se crea
        temporal.next = Nodo(data)

    # Método para eleminar nodos
    def delete(self, key):
        if self.head.data.equals(key): #Caso especial para primer dato
          self.head = self.head.next
          return
        
        temporal = self.head

        #Mientras que se esté analizando un elemento (truncado)
        while temporal.next and not temporal.next.data.equals(key): 
          #Si no es el elemento que se busca, se sigue
          temporal = temporal.next
        
        #Por si se acaba la lista (dato no encontrado)
        if not temporal.next:
          return
        
        temporal.next = temporal.next.next

        # Obtención del dato de un nodo dado su índice en la lista
    def get(self, index):
        temp = self.head
        currentpos = 0
        while(temp):
            if(index == currentpos):
                return temp
            currentpos += 1
            temp = temp.next
        return None

    #Determina si un posible nuevo nodo ya existe en la lista (SOLO PARA DATOS PRIMITIVOS)
    def contains(self, data) -> bool:
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    # Determina si un objeto está repetido en la lista (PARA INSTANCIAS DE CLASE)
    def containsObject(self, object) -> bool:
        temp = self.head
        while temp:
            #El método .equals DEBE estar definido en el objeto
            if temp.data.equals(object):
                return True
            temp = temp.next
        return False
    
    def getBy(self, key) -> Nodo:
        temp = self.head
        while(temp):
            if(temp.data.keyEquals(key)):
                return temp
            temp = temp.next
        return None

    # Método para obtener el ultimo nodo
    def getLast(self) -> Nodo:
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp

    # Método para imprimir la lista de nodos
    def printList( self ):
        node = self.head
        while node != None:
            print(node.data, end =" , ")
            node = node.next

    # Método para agregar despues de un dato en particular
    def addAfter( self, datoSeñal, newDato):
        temp = self.head
        while temp != None:
            if(temp.data == datoSeñal):
                Newnodo = Nodo(newDato)
                Newnodo.next = temp.next
                temp.next= Newnodo

            temp = temp.next

    # Método para contar elementos de la lista
    def size(self):
        if self.head:
            c = 0
            temp = self.head
            while temp:
                c += 1
                temp = temp.next
        else:
            c = 0
        return c

    # Método para agregar en un índice
    def addAt(self, data, index):

      if(index == 0): #Caso especial para primer índice
        self.head = Nodo(data, self.head)
        return
      
      if(self.head is not None): 
        temp = self.head
        #El índice está truncado a la derecha para ahorrarse una variable temporal 'previous'
        i = 1
        while(i < index):
          temp = temp.next
          if(temp is not None): i += 1
          else:
            print("Índice no encontrado.")
            return
        next = temp.next
        temp.next = Nodo(data, next)
      else:
        print("Índice no encontrado.")

    #Metodo para desvincular el nodo en el indice ingresado
    def deleteAt(self, index): #Logica similar a addAt()
      if(index == 0):
        self.head = self.head.next
        return
      if(self.head is not None):
        temp = self.head
        i = 1
        while(i < index):
          temp = temp.next
          if(temp is not None): i += 1
          else:
            print("Indice no encontrado.")
            return
        next = temp.next
        temp.next = next.next if next else None
      else:
        print("Indice no encontrado.")

    def count(self, data):
      if(self.head is not None):
        c = 0
        temp = self.head
        while(temp is not None):
          if(temp.data == data):c += 1
          temp = temp.next
      else:
        c = 0
      return c

    #Metodo que retorna una lista enlazada cuyos elementos son los indices del dato ingresado
    def indexesOf(self, data):
      indexList = LinkedList()
      if(self.head is not None):
        c = 0
        temp = self.head
        while(temp is not None):
          #El indice del elemento será el contador que cuenta todos los nodos en ese instante
          c += 1
          if(data == temp.data): indexList.agregar_al_final(c)
          temp = temp.next
      return indexList
