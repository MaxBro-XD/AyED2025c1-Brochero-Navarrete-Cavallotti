from datetime import datetime
from avl import NodoAVL, insertar_avl, buscar_avl, borrar_avl, en_rango_avl, cantidad_nodos

class Temperaturas_DB:
    def __init__(self):
        #El arbol empieza vacío sin ninguna temperatura guardada
        self.raiz = None

    def guardar_temperatura(self, temp, fecha_str):
        #Convertimos la fecha en formato texto a un objeto datetime para poder ordenarlo
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        # Insertamos la temperatura en el árbol. Si la fecha ya existía, se actualiza el valor
        self.raiz = insertar_avl(self.raiz, fecha, temp)

    def devolver_temperatura(self, fecha_str):
        #Buscamos la temperatura exacta guardada en la fecha que se pide
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        return buscar_avl(self.raiz, fecha)

    def max_temp_rango(self, f1, f2):
        #Devuelve la temperatura más alta entre dos fechas
        f1 = datetime.strptime(f1, "%d/%m/%Y")
        f2 = datetime.strptime(f2, "%d/%m/%Y")
        lista = en_rango_avl(self.raiz, f1, f2)
        return max([t for _, t in lista]) if lista else None

    def min_temp_rango(self, f1, f2):
        #Devuelve la más baja del mismo modo que max_temp_rango
        f1 = datetime.strptime(f1, "%d/%m/%Y")
        f2 = datetime.strptime(f2, "%d/%m/%Y")
        lista = en_rango_avl(self.raiz, f1, f2)
        return min([t for _, t in lista]) if lista else None

    def temp_extremos_rango(self, f1, f2):
        #Devuelve las dos temperaturas extremas (mínima y máxima) en el mismo rango
        f1 = datetime.strptime(f1, "%d/%m/%Y")
        f2 = datetime.strptime(f2, "%d/%m/%Y")
        lista = en_rango_avl(self.raiz, f1, f2)
        temps = [t for _, t in lista]
        return (min(temps), max(temps)) if temps else (None, None)

    def borrar_temperatura(self, fecha_str):
        #Elimina del árbol la temperatura registrada en la fecha dada
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = borrar_avl(self.raiz, fecha)

    def devolver_temperaturas(self, f1, f2):
        #Devuelve una lista con los registros entre dos fechas, ordenados
        f1 = datetime.strptime(f1, "%d/%m/%Y")
        f2 = datetime.strptime(f2, "%d/%m/%Y")
        lista = en_rango_avl(self.raiz, f1, f2)
        return [f"{dt.strftime('%d/%m/%Y')}: {t} °C" for dt, t in lista]

    def cantidad_muestras(self):
        #Cuenta cuántas mediciones diferentes hay en total (o sea, cuántas fechas distintas)
        return cantidad_nodos(self.raiz)
