# main.py
from modulos.mazo import Mazo
from modulos.carta import Carta
from modulos.juegoguerra import JuegoGuerra
import random

def jugar_guerra():
    # Semilla aleatoria para reproducibilidad variable
    semilla = random.randint(0, 1000)
    juego = JuegoGuerra(random_seed=semilla)
    
    # Ejecutar juego sin imprimir cada turno
    juego.iniciar_juego(ver_partida=False)
    
    print("========== RESULTADO ==========")
    print(f"Semilla utilizada: {semilla}")
    print(f"Turnos jugados: {juego.turnos_jugados}")
    
    if juego.empate:
        print("Resultado: Empate")
    else:
        print(f"Ganador: {juego.ganador}")

if __name__ == "__main__":
    jugar_guerra()
