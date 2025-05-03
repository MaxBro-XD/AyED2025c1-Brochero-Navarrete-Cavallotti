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

if __name__=="__main__":
    lista = [random.randint(10000,99999) for i in range(500)]
    print(f"Lista original: {lista}")
    quickosort(lista)
    print(f"Lista ordenada: {lista}")
