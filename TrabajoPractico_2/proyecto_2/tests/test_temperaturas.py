#Este archivo prueba todos los métodos públicos de la clase Temperaturas_DB
#La clase se importa desde el archivo temperaturas_db.py
from temperaturas_db import Temperaturas_DB

#Funciones de testeo basicas

def assert_igual(valor, esperado, mensaje):
    if valor == esperado:
        print("✓", mensaje)
    else:
        print("✖", mensaje, f"(esperado {esperado}, obtenido {valor})")

def assert_es_none(valor, mensaje):
    if valor is None:
        print("✓", mensaje)
    else:
        print("✖", mensaje, f"(esperado None, obtenido {valor})")

def assert_len(lista, esperado, mensaje):
    if len(lista) == esperado:
        print("✓", mensaje)
    else:
        print("✖", mensaje, f"(esperado {esperado} elementos, obtuvo {len(lista)})")

def main():
    db = Temperaturas_DB()

    # 1. Inserción de temperaturas
    db.guardar_temperatura(25.0, "01/01/2023")
    db.guardar_temperatura(30.5, "02/01/2023")
    db.guardar_temperatura(22.3, "03/01/2023")
    db.guardar_temperatura(27.8, "04/01/2023")
    print("Temperaturas insertadas correctamente.")

    # 2. Consulta exacta
    assert_igual(db.devolver_temperatura("02/01/2023"), 30.5, "Consulta exacta de temperatura")

    # 3. Mínimo, máximo y extremos
    t_max = db.max_temp_rango("01/01/2023", "04/01/2023")
    t_min = db.min_temp_rango("01/01/2023", "04/01/2023")
    extremos = db.temp_extremos_rango("01/01/2023", "04/01/2023")
    assert_igual(t_max, 30.5, "Temperatura máxima del rango")
    assert_igual(t_min, 22.3, "Temperatura mínima del rango")
    assert_igual(extremos, (22.3, 30.5), "Extremos del rango (mínima, máxima)")

    # 4. Listado de temperaturas ordenado
    listado = db.devolver_temperaturas("01/01/2023", "04/01/2023")
    assert_len(listado, 4, "Cantidad de temperaturas en el rango")
    print("Listado de temperaturas:")
    for linea in listado:
        print("  ", linea)

    # 5. Borrado de temperatura
    db.borrar_temperatura("02/01/2023")
    assert_es_none(db.devolver_temperatura("02/01/2023"), "Verificación posterior a borrado")

    # 6. Cantidad total de muestras
    assert_igual(db.cantidad_muestras(), 3, "Cantidad total de muestras después del borrado")

if __name__ == "__main__":
    main()
