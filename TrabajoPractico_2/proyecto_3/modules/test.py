import os
import tempfile
from difusion_palomas import DifusionPalomas

def crear_archivo_prueba():
    contenido = """Peligros,La Aparecida,10
La Aparecida,Buenas Noches,15
Buenas Noches,Cebolla,20
Cebolla,Pancrudo,30
Pancrudo,Lomaseca,25
Lomaseca,El Cerrillo,20
El Cerrillo,Malcocinado,15
Malcocinado,Aceituna,10
Malcocinado,Consuegra,5
Malcocinado,Diosleguarde,8
Diosleguarde,Elciego,10
Elciego,Melón,18"""
    temp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".txt")
    temp.write(contenido)
    temp.close()
    return temp.name

def test_difusion():
    path = crear_archivo_prueba()
    try:
        sistema = DifusionPalomas(path)
        sistema.construir_mst()
        sistema.generar_difusion()

        assert "Peligros" in sistema.padres
        assert sistema.padres["La Aparecida"] == "Peligros"
        assert "Aceituna" in sistema.hijos["Malcocinado"]
        assert sistema.distancia_total > 0

        print("Test de difusión superado correctamente")
    except AssertionError as e:
        print("Error en el test de difusión")
        raise e
    finally:
        os.remove(path)

if __name__ == "__main__":
    test_difusion()
