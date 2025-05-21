# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

import random
def bubble_sort(lista):
    for i in range(len(lista)-1, 0, -1):
        for x in range(i):
            if lista[x]>lista[x+1]:
                lista[x], lista[x+1]= lista[x+1], lista[x]
    return lista

# ----------------------
# Prueba del algoritmo
# ----------------------
if __name__=="__main__":
    # Generar 500 números aleatorios de 5 dígitos (entre 10000 y 99999)
    lista_numeros = [random.randint(10000, 99999) for _ in range(500)]

    # Copia para comparar después
    original = lista_numeros.copy()

    # Ordenar con bubble_sort
    bubble_sort(lista_numeros)

    # Verificar si está ordenado correctamente
    if lista_numeros == sorted(original):
        print(" La lista está ordenada correctamente con Bubble_sort.")
    else:
        print(" Error: la lista no está ordenada correctamente.")

