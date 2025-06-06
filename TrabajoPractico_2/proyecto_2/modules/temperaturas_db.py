from modules.arbol_busqueda import AVL
import datetime

class Temperaturas_DB:
    def __init__(self):
        self.db = AVL()

    def insertar(self, ciudad, temperatura):
        self.db.insertar(ciudad, temperatura)

    def eliminar(self, ciudad):
        self.db.eliminar(ciudad)

    def buscar(self, ciudad):
        return self.db.buscar(ciudad)

    def actualizar(self, ciudad, nueva_temperatura):
        if self.db.buscar(ciudad) is not None:
            self.db.insertar(ciudad, nueva_temperatura)
        else:
            raise ValueError("Ciudad no encontrada en la base de datos.")
    
    def guardar_temperaturas(self):
        