
import random
import time
import matplotlib.pyplot as plt

# ---------- ORDENAMIENTO BURBUJA ----------
def bubble_sort(lista):
    for i in range(len(lista)-1, 0, -1):
        for x in range(i):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]
    return lista

# ---------- QUICKSORT ----------
def quickosort(lista):
    quicksortAuxiliar(lista, 0, len(lista)-1)
    return lista

def quicksortAuxiliar(lista, primero, ultimo):
    if primero < ultimo:
        puntoDivision = particion(lista, primero, ultimo)
        quicksortAuxiliar(lista, primero, puntoDivision-1)
        quicksortAuxiliar(lista, puntoDivision+1, ultimo)

def particion(lista, primero, ultimo):
    valorPivote = lista[primero]
    marcaIzq = primero + 1
    marcaDer = ultimo
    hecho = False
    while not hecho:
        while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
            marcaIzq += 1
        while marcaDer >= marcaIzq and lista[marcaDer] >= valorPivote:
            marcaDer -= 1
        if marcaDer < marcaIzq:
            hecho = True
        else:
            lista[marcaIzq], lista[marcaDer] = lista[marcaDer], lista[marcaIzq]
    lista[primero], lista[marcaDer] = lista[marcaDer], lista[primero]
    return marcaDer

# ---------- RADIX SORT ----------
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

# ---------- PRUEBA Y TIEMPOS ----------
tamaños = [500, 1000, 2000]  # Puedes modificar estos tamaños si deseas
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
