import random
def quickosort(lista):
   quicksortAuxiliar(lista,0,len(lista)-1)
   return lista

def quicksortAuxiliar(lista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = particion(lista,primero,ultimo)

       quicksortAuxiliar(lista,primero,puntoDivision-1)
       quicksortAuxiliar(lista,puntoDivision+1,ultimo)


def particion(lista,primero,ultimo):
   valorPivote = lista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = lista[marcaIzq]
           lista[marcaIzq] = lista[marcaDer]
           lista[marcaDer] = temp

   temp = lista[primero]
   lista[primero] = lista[marcaDer]
   lista[marcaDer] = temp


   return marcaDer

# ----------------------
# Prueba del algoritmo
# ----------------------
if __name__=="__main__":
    # Generar 500 números aleatorios de 5 dígitos (entre 10000 y 99999)
    lista_numeros = [random.randint(10000, 99999) for _ in range(500)]

    # Copia para comparar después
    original = lista_numeros.copy()

    # Ordenar con quicksort
    quickosort(lista_numeros)
    
    # Verificar si está ordenado correctamente
    if lista_numeros == sorted(original):
        print(" La lista está ordenada correctamente con Quicksort.")
    else:
        print(" Error: la lista no está ordenada correctamente.")
