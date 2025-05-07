import time
import matplotlib.pyplot as plt
import numpy as np
from modulos import LDE
from LDE import ListaDobleEnlazada
# Función para medir el tiempo de ejecución de cada método
def medir_tiempo_metodo(lista, metodo, *args):
    start = time.time()
    getattr(lista, metodo)(*args)
    end = time.time()
    return end - start

# Crear listas de diferentes tamaños
tamanios = np.arange(1, 1001, 10)  # Tamaños de 1 a 1000
tiempos_len = []
tiempos_copy = []
tiempos_reverse = []

for tamano in tamanios:
    lista = ListaDobleEnlazada()
    
    # Llenar la lista con datos 
    for i in range(tamano):
        lista.agregar_al_final(i)
    
    # Medir tiempo de ejecución para cada método
    tiempos_len.append(medir_tiempo_metodo(lista, "__len__"))
    tiempos_copy.append(medir_tiempo_metodo(lista, "copiar"))
    tiempos_reverse.append(medir_tiempo_metodo(lista, "invertir"))

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(tamanios, tiempos_len, label='len', color='blue')
plt.plot(tamanios, tiempos_copy, label='copiar', color='green')
plt.plot(tamanios, tiempos_reverse, label='invertir', color='red')

plt.xlabel('Tamaño de la lista (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('N vs Tiempo de Ejecución')
plt.legend()
plt.grid(True)
plt.show()
