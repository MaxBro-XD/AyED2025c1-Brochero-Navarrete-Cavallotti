from datetime import datetime
from modules.arbol_busqueda import AVL

class Temperaturas_DB:
    def __init__(self):
        self.arbol = AVL()

    def guardar_temperatura(self, temperatura, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        self.arbol.agregar(fecha_obj, temperatura)

    def devolver_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        return self.arbol.obtener(fecha_obj)

    def borrar_temperatura(self, fecha):
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        self.arbol.eliminar(fecha_obj)

    def cantidad_muestras(self):
        return self.arbol.longitud()

    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")
        resultados = []

        def recorrido_en_rango(nodo):
            if nodo is None:
                return
            if nodo.clave >= f1:
                recorrido_en_rango(nodo.hijoIzquierdo)
            if f1 <= nodo.clave <= f2:
                resultados.append(nodo)
            if nodo.clave <= f2:
                recorrido_en_rango(nodo.hijoDerecho)

        recorrido_en_rango(self.arbol.raiz)
        resultados.sort(key=lambda nodo: nodo.clave)
        return [f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.cargaUtil} ºC" for nodo in resultados]

    def max_temp_rango(self, fecha1, fecha2):
        temps = self._obtener_temperaturas_en_rango(fecha1, fecha2)
        return max(temps) if temps else None

    def min_temp_rango(self, fecha1, fecha2):
        temps = self._obtener_temperaturas_en_rango(fecha1, fecha2)
        return min(temps) if temps else None

    def temp_extremos_rango(self, fecha1, fecha2):
        temps = self._obtener_temperaturas_en_rango(fecha1, fecha2)
        return (min(temps), max(temps)) if temps else (None, None)

    def _obtener_temperaturas_en_rango(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = []

        def recorrer(nodo):
            if nodo is None:
                return
            if nodo.clave >= f1:
                recorrer(nodo.hijoIzquierdo)
            if f1 <= nodo.clave <= f2:
                temperaturas.append(nodo.cargaUtil)
            if nodo.clave <= f2:
                recorrer(nodo.hijoDerecho)

        recorrer(self.arbol.raiz)
        return temperaturas


# -------------------------------
# PRUEBA DEL FUNCIONAMIENTO
# -------------------------------
if __name__ == "__main__":
    db = Temperaturas_DB()

    db.guardar_temperatura(23.5, "01/06/2025")
    db.guardar_temperatura(24.1, "02/06/2025")
    db.guardar_temperatura(21.9, "03/06/2025")
    db.guardar_temperatura(19.8, "04/06/2025")

    print("Cantidad de muestras:", db.cantidad_muestras())

    print("Temperatura 02/06/2025:", db.devolver_temperatura("02/06/2025"))

    print("Temperaturas entre 01/06 y 03/06:")
    for linea in db.devolver_temperaturas("01/06/2025", "03/06/2025"):
        print("  ", linea)

    print("Temperatura mínima entre 01/06 y 04/06:", db.min_temp_rango("01/06/2025", "04/06/2025"))
    print("Temperatura máxima entre 01/06 y 04/06:", db.max_temp_rango("01/06/2025", "04/06/2025"))
    print("Extremos entre 01/06 y 04/06:", db.temp_extremos_rango("01/06/2025", "04/06/2025"))

    print("Borrando temperatura de 03/06/2025...")
    db.borrar_temperatura("03/06/2025")

    print("Cantidad de muestras:", db.cantidad_muestras())