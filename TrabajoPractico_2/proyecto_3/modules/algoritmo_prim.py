import sys
from modules.cola_prioridad import ColaConPrioridad
from modules.grafo import Grafo

def prim(grafo, inicio):
    distancia = {}
    padre = {}
    visitado = set()
    cp = ColaConPrioridad()

    for nodo in grafo.obtener_vertices():
        distancia[nodo] = sys.maxsize
        padre[nodo] = None

    distancia[inicio] = 0
    cp.append(0, inicio)

    while len(cp) > 0:
        actual = cp.pop()

        if actual in visitado:
            continue
        visitado.add(actual)

        for vecino, peso in grafo.obtener_vecinos(actual):
            if vecino not in visitado and peso < distancia[vecino]:
                distancia[vecino] = peso
                padre[vecino] = actual
                cp.append(peso, vecino)

    return padre, distancia

if __name__ == "__main__":
    # Prueba mínima
    grafo = Grafo()
    grafo.agregar_arista("A", "B", 4)
    grafo.agregar_arista("A", "C", 1)
    grafo.agregar_arista("C", "B", 2)
    grafo.agregar_arista("B", "D", 1)
    grafo.agregar_arista("C", "D", 5)

    padre, distancia = prim(grafo, "A")

    print("Árbol de expansión mínima desde A:")
    for nodo in sorted(padre.keys()):
        print(f"{nodo} ← {padre[nodo]} (distancia: {distancia[nodo]})")

    total = sum(distancia[n] for n in distancia if padre[n] is not None)
    print(f"\nDistancia total del árbol: {total}")