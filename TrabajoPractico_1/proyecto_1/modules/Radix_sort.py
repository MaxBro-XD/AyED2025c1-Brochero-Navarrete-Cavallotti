
#Implementar en phyton el algoritmo de ordenamiento, ordenamiento
#por residuos (radix sort)
import random
def radix_sort(arr):
    # Encuentra el número con más dígitos
    max_num = max(arr)
    exp = 1  # 1, 10, 100, 1000, etc.

    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

# ----------------------
# Counting Sort by Digit
# ----------------------
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Para los dígitos del 0 al 9

    # Contar ocurrencias de cada dígito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Sumar acumulativamente
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo ordenado (de forma estable)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copiar al arreglo original
    for i in range(n):
        arr[i] = output[i]

# ----------------------
# Prueba del algoritmo
# ----------------------

# Generar 500 números aleatorios de 5 dígitos (entre 10000 y 99999)
lista_numeros = [random.randint(10000, 99999) for _ in range(500)]

# Copia para comparar después
original = lista_numeros.copy()

# Ordenar con radix sort
radix_sort(lista_numeros)

# Verificar si está ordenado correctamente
if lista_numeros == sorted(original):
    print(" La lista está ordenada correctamente con Radix Sort.")
else:
    print(" Error: la lista no está ordenada correctamente.")
