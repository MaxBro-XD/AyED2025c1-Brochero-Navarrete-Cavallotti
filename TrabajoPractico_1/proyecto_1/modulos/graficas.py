#graficas
import random
import time
import matplotlib.pyplot as plt
from modulos.bubble_sort import bubble_sort
from modulos.quicksort import quickosort  
from modulos.radixsort import radix_sort

# ---------- PRUEBA Y TIEMPOS ----------
# tamaños = range(1,1000,50)  # Puedes modificar estos tamaños si deseas
tamaños = [_ for _ in range(1,1000,50)]
tiempos_burbuja = []
tiempos_quick = []
tiempos_radix = []

for n in tamaños:
    lista = [random.randint(10000, 99999) for _ in range(n)]

    l1 = lista.copy()
    inicio = time.time()
    bubble_sort(l1)
    tiempos_burbuja.append(time.time() - inicio)

    l2 = lista.copy()
    inicio = time.time()
    quickosort(l2)
    tiempos_quick.append(time.time() - inicio)

    l3 = lista.copy()
    inicio = time.time()
    radix_sort(l3)
    tiempos_radix.append(time.time() - inicio)

# ---------- GRAFICAR ----------
plt.figure(figsize=(10,6))
plt.plot(tamaños, tiempos_burbuja, marker='o', label='Burbuja (O(n²))')
plt.plot(tamaños, tiempos_quick, marker='o', label='Quicksort (O(n log n))')
plt.plot(tamaños, tiempos_radix, marker='o', label='Radix Sort (O(nk))')
plt.title('Comparación de Tiempos de Ordenamiento')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()