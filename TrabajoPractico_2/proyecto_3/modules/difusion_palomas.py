from modules.grafo import Grafo
from modules.algoritmo_prim import prim

def cargar_grafo_desde_archivo(ruta_archivo):
    grafo = Grafo()
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) == 3:
                origen = partes[0].strip()
                destino = partes[1].strip()
                peso = int(partes[2].strip())
                grafo.agregar_arista(origen, destino, peso)
    return grafo

def invertir_diccionario(padres):
    hijos = {k: [] for k in padres}
    for aldea, padre in padres.items():
        if padre is not None:
            hijos[padre].append(aldea)
    return hijos

def mostrar_resultado(padres, distancias):
    aldeas = sorted(padres.keys())
    hijos = invertir_diccionario(padres)

    print("\nLista de aldeas en orden alfabético:\n")
    for aldea in aldeas:
        print(aldea)
    
    print("\nDifusión de mensajes:\n")
    print(f"{'Aldea':<20} {'Recibe de':<15} {'Envía a'}")
    print("-" * 60)
    for aldea in aldeas:
        recibe = padres[aldea] if padres[aldea] is not None else "-"
        envia_a = ", ".join(sorted(hijos[aldea])) if hijos[aldea] else "-"
        print(f"{aldea:<20} {recibe:<15} {envia_a}")

    distancia_total = sum(distancias[aldea] for aldea in distancias if padres[aldea] is not None)
    print(f"\nDistancia total recorrida por las palomas: {distancia_total} leguas")

if __name__ == "__main__":
    ruta_archivo = "aldeas.txt"  # Modificá esta ruta si tenés el archivo en otro lugar
    grafo = cargar_grafo_desde_archivo(ruta_archivo)

    aldea_origen = "Peligros"
    padres, distancias = prim(grafo, aldea_origen)

    mostrar_resultado(padres, distancias)
