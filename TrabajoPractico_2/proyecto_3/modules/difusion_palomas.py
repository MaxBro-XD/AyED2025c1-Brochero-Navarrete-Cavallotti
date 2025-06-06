from collections import defaultdict, deque

class DifusionPalomas:
    def __init__(self, archivo):
        """Inicializa la clase leyendo el archivo y construyendo el grafo."""
        self.grafo = defaultdict(list)
        self.mst = defaultdict(list)
        self.padres = {}
        self.hijos = defaultdict(list)
        self.distancia_total = 0
        self.origen = "Peligros"
        self._leer_archivo(archivo)

    def _leer_archivo(self, archivo):
        """Lee el archivo de texto y construye el grafo con validaciones."""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for nro_linea, linea in enumerate(f, start=1):
                    partes = linea.strip().split(",")
                    if len(partes) == 3:
                        a, b = partes[0].strip(), partes[1].strip()
                        try:
                            distancia = int(partes[2])
                            self.grafo[a].append((b, distancia))
                            self.grafo[b].append((a, distancia))
                        except ValueError:
                            print(f"⚠️ Línea {nro_linea} ignorada (distancia no numérica): {linea.strip()}")
                    else:
                        print(f"⚠️ Línea {nro_linea} ignorada (mal formateada): {linea.strip()}")
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{archivo}' no fue encontrado.")

    def construir_mst(self):
        """Construye el árbol de expansión mínima usando el algoritmo de Prim."""
        visitados = set()
        visitados.add(self.origen)
        bordes = [(dist, self.origen, destino) for destino, dist in self.grafo[self.origen]]

        while bordes:
            bordes.sort()
            dist, origen, destino = bordes.pop(0)
            if destino not in visitados:
                visitados.add(destino)
                self.mst[origen].append((destino, dist))
                self.mst[destino].append((origen, dist))
                self.distancia_total += dist
                for vecino, d in self.grafo[destino]:
                    if vecino not in visitados:
                        bordes.append((d, destino, vecino))

    def generar_difusion(self):
        """Genera la estructura de difusión BFS desde la aldea origen."""
        visitados = set()
        cola = deque([self.origen])
        self.padres[self.origen] = None

        while cola:
            actual = cola.popleft()
            visitados.add(actual)
            for vecino, _ in sorted(self.mst[actual]):
                if vecino not in visitados:
                    self.padres[vecino] = actual
                    self.hijos[actual].append(vecino)
                    cola.append(vecino)

    def mostrar_resultados(self):
        """Imprime los resultados de la difusión."""
        print("\n Aldeas en orden alfabético:\n")
        for aldea in sorted(self.mst.keys()):
            print(aldea)

        print("\n Difusión del mensaje:\n")
        for aldea in sorted(self.mst.keys()):
            print(f"Aldea: {aldea}")
            if self.padres[aldea] is not None:
                print(f"  Recibe de: {self.padres[aldea]}")
            else:
                print("  Recibe de: - (origen)")
            if self.hijos[aldea]:
                print(f"  Envía a: {', '.join(sorted(self.hijos[aldea]))}")
            else:
                print("  Envía a: ninguna")

        print(f"\n Distancia total recorrida por las palomas: {self.distancia_total} leguas")

if __name__ == "__main__":
    sistema = DifusionPalomas("aldeas.txt")
    sistema.construir_mst()
    sistema.generar_difusion()
    sistema.mostrar_resultados()
