from modules.temperaturas_db import Temperaturas_DB

def main():
    db = Temperaturas_DB()

    # Agregar temperaturas
    db.guardar_temperatura(23.5, "01/06/2025")
    db.guardar_temperatura(24.1, "02/06/2025")
    db.guardar_temperatura(21.9, "03/06/2025")
    db.guardar_temperatura(19.8, "04/06/2025")

    # Mostrar cantidad total de muestras
    print("Cantidad de muestras:", db.cantidad_muestras())

    # Mostrar temperatura específica
    print("Temperatura 02/06/2025:", db.devolver_temperatura("02/06/2025"))

    # Mostrar temperaturas en un rango
    print("Temperaturas entre 01/06 y 03/06:")
    for linea in db.devolver_temperaturas("01/06/2025", "03/06/2025"):
        print("  ", linea)

    # Mostrar extremos
    print("Temperatura mínima entre 01/06 y 04/06:", db.min_temp_rango("01/06/2025", "04/06/2025"))
    print("Temperatura máxima entre 01/06 y 04/06:", db.max_temp_rango("01/06/2025", "04/06/2025"))
    print("Extremos entre 01/06 y 04/06:", db.temp_extremos_rango("01/06/2025", "04/06/2025"))

    # Borrar una muestra
    print("Borrando temperatura de 03/06/2025...")
    db.borrar_temperatura("03/06/2025")

    print("Cantidad de muestras:", db.cantidad_muestras())

if __name__ == "__main__":
    main()