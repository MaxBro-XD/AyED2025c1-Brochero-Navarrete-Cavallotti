# mazo

from modulos.LDE import ListaDobleEnlazada
from modulos.carta import Carta

class DequeEmptyError(Exception):
    def __init__(self, mensaje="El mazo está vacío"):
        super().__init__(mensaje)
    
class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        
        if self._cartas.estavacia():
            raise DequeEmptyError("El mazo está vacío")
        carta = self._cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def __len__(self):
        return len(self._cartas)

    def __str__(self):
        return str(self._cartas)

    def __repr__(self):
        return str(self)
    
if __name__ == "__main__":
    mazo = Mazo()
    carta1 = Carta("7", "♠")
    carta2 = Carta("K", "♦")
    mazo.poner_carta_arriba(carta1)
    mazo.poner_carta_abajo(carta2)
    print("Contenido del mazo:", mazo)
    carta_extraida = mazo.sacar_carta_arriba(mostrar=True)
    print("Carta extraída:", carta_extraida)
    print("Contenido restante del mazo:", mazo)
