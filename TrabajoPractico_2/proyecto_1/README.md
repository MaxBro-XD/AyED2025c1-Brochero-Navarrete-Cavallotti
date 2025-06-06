🕊️🩺🌡️ **Ordenando el Caos** 🌡️🩺🕊️


📄 **Breve descripción del proyecto**

Este proyecto aborda tres situaciones distintas modeladas con estructuras de datos específicas y eficientes:
- Gestión de pacientes en una sala de emergencias mediante una cola de prioridad basada en montículo binario.
- Registro y consulta de temperaturas a lo largo del tiempo utilizando un árbol AVL.
- Difusión de mensajes entre aldeas mediante la construcción de un árbol generador mínimo y recorrido BFS.
Cada aplicación busca resolver problemas reales utilizando estructuras que optimizan la búsqueda, inserción, eliminación y recorrido de datos.


🏗  **Arquitectura General**

El código está organizado en tres proyectos independientes:
- Proyecto 1 (Sala de emergencias): incluye clases genéricas para la cola de prioridad (montículo binario) y una clase de pacientes.
- Proyecto 2 (Temperaturas): contiene la implementación del árbol AVL y una clase 'Temperaturas_DB' que gestiona las operaciones requeridas.
- Proyecto 3 (Aldeas): trabaja con estructuras de grafos no dirigidos y aplica los algoritmos de Prim y BFS.
Cada proyecto está organizado en una carpeta propia, con sus respectivos módulos, pruebas unitarias y documentación.
Los informes y testeos correspondientes están ubicados en la carpeta 'modulos' de cada proyecto.


📑  **Dependencias**

• Python 3.x
• datetime (módulo estándar)
• collections (módulo estándar)
No se requiere instalación de bibliotecas externas. 


🚀  **Cómo Ejecutar el Proyecto**

1. Clonar o descargar el repositorio.
2. Ingresar a la carpeta del proyecto correspondiente.

3. Para ejecutar cada proyecto:

   - Proyecto 1 (Sala de Emergencias):
     Ejecutar el archivo `test_sala_emergencias.py` para comprobar el funcionamiento de la estructura de triaje.

   - Proyecto 2 (Temperaturas):
     Ejecutar `test_temperaturas.py` para validar la base de datos basada en árbol AVL.

   - Proyecto 3 (Difusión entre Aldeas):
     Ejecutar el archivo `difusion_palomas.py`, asegurándose de tener `aldeas.txt` en el mismo directorio. El archivo imprimirá por consola el recorrido de difusión y la distancia total recorrida.

