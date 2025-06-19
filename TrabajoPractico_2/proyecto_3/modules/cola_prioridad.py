from modules.monticulo_binario import MonticuloBinario

class ColaConPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.contador = 0  # Para desempatar prioridades iguales

    def append(self, prioridad, dato):
        self.monticulo.insertar((prioridad, self.contador, dato))
        self.contador += 1

    def pop(self):
        _, _, dato = self.monticulo.eliminarMin()
        return dato

    def __len__(self):
        return self.monticulo.tamanoActual

    def __iter__(self):
        copia = MonticuloBinario()
        copia.construirMonticulo(self.monticulo.listaMonticulo[1:])
        while copia.tamanoActual > 0:
            _, _, dato = copia.eliminarMin()
            yield dato

if __name__ == "__main__":
    print("Probando ColaConPrioridad con valores genéricos (peso, nodo):\n")

    cola = ColaConPrioridad()
    valores = [(3, 'A'), (1, 'B'), (4, 'C'), (2, 'D')]

    for peso, nodo in valores:
        print(f"Agregando nodo {nodo} con peso {peso}")
        cola.append(peso, nodo)

    print("\nExtrayendo nodos en orden de prioridad:\n")
    while len(cola) > 0:
        nodo = cola.pop()
        print(f"Nodo extraído: {nodo}")