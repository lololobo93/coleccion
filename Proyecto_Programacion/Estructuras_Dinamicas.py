"""
    Metodos de Pila y Cola para usar en el codigo principal.

"""

"Definicion de Pila con sus respectivas funciones."
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self, num_i):
         return self.items.pop(num_i)

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
    
     def llena(self):
         return (len(self.items) >= 10)

     def __iter__(self):
         for id in self.items:
             yield id

"Definicion de Cola con sus respectivas funciones."
class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def agregar_final(self, item):
        self.items.append(item)

    def avanzar(self):
        return self.items.pop()
    
    def eliminar(self, num_i):
        return self.items.pop(num_i)

    def tamano(self):
        return len(self.items)

    def __iter__(self):
         for id in self.items[::-1]:
             yield id