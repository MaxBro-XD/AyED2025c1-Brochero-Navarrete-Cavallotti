

class Nodo:
    def __init__(self, dato, prioridad, orden_llegada):
        self.dato = dato
        self.prioridad = (prioridad, orden_llegada)  # tupla para desempate

class ColaConPrioridad:
    def __init__(self):
        self.elementos = []
        self.contador = 0  # orden de llegada

    def append(self, dato):
        # El objeto `dato` es un paciente, usamos su riesgo como prioridad
        riesgo = dato.get_riesgo()
        nodo = Nodo(dato, riesgo, self.contador)
        self.contador += 1
        self.elementos.append(nodo)
        self.elementos.sort(key=lambda x: x.prioridad)  # menor riesgo y más temprano primero

    def pop(self, index=0):
        return self.elementos.pop(index).dato

    def __len__(self):
        return len(self.elementos)

    def __iter__(self):
        return (nodo.dato for nodo in self.elementos)

    def __getitem__(self, index):
        return self.elementos[index].dato
