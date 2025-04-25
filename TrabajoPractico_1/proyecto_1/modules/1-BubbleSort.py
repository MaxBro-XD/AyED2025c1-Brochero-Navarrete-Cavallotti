# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

import random
lista1=[random.randint(10000,99999) for i in range(500)]
print (f"lista original: {lista1}")
def bubble_sort(lista):
    for i in range(len(lista)-1, 0, -1):
        for x in range(i):
            if lista[x]>lista[x+1]:
                lista[x], lista[x+1]= lista[x+1], lista[x]
    return lista

r=bubble_sort(lista1)
print(f"lista ordenada: {r}")
        

            



