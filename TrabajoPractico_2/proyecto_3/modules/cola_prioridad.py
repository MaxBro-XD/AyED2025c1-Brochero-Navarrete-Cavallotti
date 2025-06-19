from modules.paciente import Paciente
from modules.monticulo_binario import MonticuloBinario
import time

class ColaConPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.contador = 0  # Para desempatar por orden de llegada

    def append(self, dato):
        riesgo = dato.get_riesgo()
        # Insertamos directamente la tupla en el montículo
        self.monticulo.insertar((riesgo, self.contador, dato))
        self.contador += 1

    def pop(self):
        # Sacamos el de mayor prioridad (menor riesgo y más antiguo)
        _, _, dato = self.monticulo.eliminarMin()
        return dato

    def __len__(self):
        return self.monticulo.tamanoActual

    def __iter__(self):
        # Iterador sin destruir el montículo original
        copia = MonticuloBinario()
        copia.construirMonticulo(self.monticulo.listaMonticulo[1:])
        while copia.tamanoActual > 0:
            _, _, dato = copia.eliminarMin()
            yield dato

if __name__ == "__main__":

    cola = ColaConPrioridad()

    print("Generando 5 pacientes aleatorios...\n")

    for i in range(5):
        paciente = Paciente()
        print(f"Paciente {i+1}:{paciente}\n")
        cola.append(paciente)
        time.sleep(1)

    print("\n Atendiendo pacientes en orden de prioridad \n")
    while len(cola) > 0:
        atendido = cola.pop()
        print(f"Atendido:{atendido}\n")