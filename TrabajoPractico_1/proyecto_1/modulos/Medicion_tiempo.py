import random
import time
import matplotlib.pyplot as plt

from modulos.BubbleSort import bubble_sort 
from modulos.Quicksort import quickosort
from modulos.Radix_sort import radix_sort

tamanos = list(range(10, 1001, 50))
tiempos_bubble = []
tiempos_quick = []
tiempos_radix = []

for n in tamanos:
    lista_base = [random.randint(10000, 99999) for _ in range(n)]

    # Bubble Sort
    lista = lista_base[:]
    inicio = time.time()
    bubble_sort(lista)
    tiempos_bubble.append(time.time() - inicio)

    # Quick Sort
    lista = lista_base[:]
    inicio = time.time()
    quickosort(lista)
    tiempos_quick.append(time.time() - inicio)

    # Radix Sort
    lista = lista_base[:]
    inicio = time.time()
    radix_sort(lista)
    tiempos_radix.append(time.time() - inicio)


# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_bubble, label='Bubble Sort', color='red')
plt.plot(tamanos, tiempos_quick, label='Quick Sort', color='blue')
plt.plot(tamanos, tiempos_radix, label='Radix Sort', color='green')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()