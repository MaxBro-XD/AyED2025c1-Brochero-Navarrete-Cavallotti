# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

import random
def bubble_sort(lista):
    for i in range(len(lista)-1, 0, -1):
        for x in range(i):
            if lista[x]>lista[x+1]:
                lista[x], lista[x+1]= lista[x+1], lista[x]
    return lista

if __name__=="__main__":
    lista=[random.randint(10000,99999) for i in range(500)]
    print (f"Lista original: {lista}")
    r=bubble_sort(lista)
    print(f"Lista ordenada: {r}")
        
