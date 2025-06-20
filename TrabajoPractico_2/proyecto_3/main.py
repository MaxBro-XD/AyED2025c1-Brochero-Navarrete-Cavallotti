from modules.difusion_palomas import cargar_grafo_desde_archivo, mostrar_resultado
from modules.algoritmo_prim import prim

def main():
    ruta_archivo = "aldeas.txt"  # Ajustá si está en otra carpeta
    grafo = cargar_grafo_desde_archivo(ruta_archivo)

    aldea_origen = "Peligros"
    padres, distancias = prim(grafo, aldea_origen)

    mostrar_resultado(padres, distancias)

if __name__ == "__main__":
    main()