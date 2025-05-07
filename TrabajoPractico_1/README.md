
   ⚔️🔥🧠   ALGORITMOS EN GUERRA   ⚔️🔥🧠   

TRABAJO PRÁCTICO 1 – Algoritmos y Estructuras de Datos - CAVALLOTTI, NAVARRETE, BROCHERO

Este proyecto contiene la resolución completa del Trabajo Práctico Nº1 de la materia AyED. Se divide en tres secciones principales: 
algoritmos de ordenamiento, implementación de una lista doblemente enlazada como TAD, y la simulación del juego de cartas “Guerra” utilizando estructuras creadas previamente.

---

## 🏗 Arquitectura General

📁 `TrabajoPractico_1/proyecto_1`  
Contiene la implementación de tres algoritmos de ordenamiento:  
- Burbuja  
- Quicksort  
- Radix sort  

Además, se incluye un script para:
- Generar listas aleatorias de 5 dígitos (500 a 1000 elementos)
- Medir tiempos de ejecución
- Comparar con el algoritmo `sorted()` de Python
- Graficar los resultados obtenidos

📁 `TrabajoPractico_1/proyecto_2`  
Implementación de la clase `ListaDobleEnlazada`, que incluye:
- Métodos especificados por la cátedra: agregar, extraer, copiar, invertir, concatenar, etc.
- Manejo de excepciones para inserciones o extracciones inválidas
- Gráficas de tiempo de ejecución de los métodos `len`, `copiar` e `invertir`
- Código compatible con los tests oficiales provistos

📁 `TrabajoPractico_1/proyecto_3`  
Simulación completa del juego de cartas “Guerra”, utilizando:
- `Carta`: clase que representa una carta
- `Mazo`: clase que modela un mazo usando la lista doblemente enlazada del punto 2
- `JuegoGuerra`: lógica del juego, guerras, turnos, ganador, empate
- `main.py`: script para ejecutar automáticamente una partida

📁 `TrabajoPractico_1`  
Incluye el informe PDF del trabajo, con:
- Análisis de complejidad teórico y experimental
- Gráficos generados
- Explicaciones de diseño y decisiones tomadas

📁 `TrabajoPractico_1/proyecto_1/main.py`  
Gráficos y archivos generados por los algoritmos de ordenamiento.

📁 `TrabajoPractico_1/proyecto_2/main.py` 
Gráfica análisis de métodos LDE.
---

## 📑 Dependencias

- Python 3.x
- matplotlib (solo para graficar en problemas 1 y 2)
- time (módulo estándar de Python)


## 🚀 Cómo Ejecutar el Proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/MaxBro-XD/AyED2025c1-Brochero-Navarrete-Cavallotti.git

2. Crear y activar un entorno virtual:
python -m venv env
source env/bin/activate  # en Windows: env\Scripts\activate

3.Instalar las dependencias:
pip install -r deps/requirements.txt

4.Para ejecutar cada parte:

   A) Ordenamientos:
cd TrabajoPractico_1/proyecto_1
python main.py

   B) LDE:
cd TrabajoPractico_1/proyecto_2
python test_lde.py  # o correr el script principal si hay

   C) Juego guerra:
cd TrabajoPractico_1/proyecto_3
python main.py

---
## 🙎‍♀️🙎‍♂️Autores

- Apellido y Nombre del primer integrante: Caterina Navarrete
- Apellido y Nombre del segundo integrante Guadalupe Cavallotti
- Apellido y Nombre del primer integrante: Maximo Brochero

