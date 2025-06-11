from modules.arbol_busqueda import AVL
import datetime

class Temperaturas_DB:
    def __init__(self):
        self.arbol = AVL()

    def guardar_temperatura(self, temperatura, fecha):
        self.arbol.agregar(fecha, temperatura)

    def devolver_temperatura(self, fecha):
        nodo = self.arbol.obtener(fecha)
        if nodo:
            return nodo.res 
        return None

    def borrar_temperatura(self, fecha):
        self.arbol.eliminar(fecha)

    def cantidad_muestras(self):
        return self.arbol.contar_nodos()

    def devolver_temperaturas(self, fecha1, fecha2):
        nodos_en_rango = self.arbol.obtener_rango(fecha1, fecha2)
        return [f"{fecha}: {temp} ºC" for fecha, temp in nodos_en_rango]

    def max_temp_rango(self, fecha1, fecha2):
        nodos_en_rango = self.arbol.obtener_rango(fecha1, fecha2)
        if not nodos_en_rango:
            return None
        return max(temp for _, temp in nodos_en_rango)

    def min_temp_rango(self, fecha1, fecha2):
        nodos_en_rango = self.arbol.obtener_rango(fecha1, fecha2)
        if not nodos_en_rango:
            return None
        return min(temp for _, temp in nodos_en_rango)

    def temp_extremos_rango(self, fecha1, fecha2):
        nodos_en_rango = self.arbol.obtener_rango(fecha1, fecha2)
        if not nodos_en_rango:
            return (None, None)
        temperaturas = [temp for _, temp in nodos_en_rango]
        return (min(temperaturas), max(temperaturas))    


if __name__ == "__main__":
    db = Temperaturas_DB()
    db.guardar_temperatura(23.5, "01/06/2025")
    db.guardar_temperatura(21.0, "02/06/2025")
    db.guardar_temperatura(25.2, "03/06/2025")
    db.guardar_temperatura(19.4, "04/06/2025")

    print("Temperatura el 02/06/2025:", db.devolver_temperatura("02/06/2025"))
    print("Temperaturas entre 01/06/2025 y 04/06/2025:")
    for t in db.devolver_temperaturas("01/06/2025", "04/06/2025"):
        print(t)
    print("Temperatura máxima en el rango:", db.max_temp_rango("01/06/2025", "04/06/2025"))
    print("Temperatura mínima en el rango:", db.min_temp_rango("01/06/2025", "04/06/2025"))
    print("Extremos de temperatura en el rango:", db.temp_extremos_rango("01/06/2025", "04/06/2025"))

    db.borrar_temperatura("02/06/2025")
    print("Cantidad de muestras después de borrar:", db.cantidad_muestras())