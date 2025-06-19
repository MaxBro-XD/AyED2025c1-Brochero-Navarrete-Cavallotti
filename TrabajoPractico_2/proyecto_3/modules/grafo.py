class Grafo:
    def __init__(self):
        self.adyacencias = {}

    def agregar_arista(self, origen, destino, peso):
        # Asegura que las listas existan
        self.adyacencias.setdefault(origen, []).append((destino, peso))
        self.adyacencias.setdefault(destino, []).append((origen, peso))

    def obtener_vertices(self):
        return list(self.adyacencias.keys())

    def obtener_vecinos(self, nodo):
        return self.adyacencias.get(nodo, [])

if __name__ == "__main__":
    # Prueba mínima de grafo
    grafo = Grafo()
    grafo.agregar_arista("X", "Y", 10)
    grafo.agregar_arista("Y", "Z", 5)
    grafo.agregar_arista("X", "Z", 3)

    for v in grafo.obtener_vertices():
        print(f"{v}: {grafo.obtener_vecinos(v)}")