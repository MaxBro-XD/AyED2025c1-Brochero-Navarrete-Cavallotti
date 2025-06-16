import unittest
from modules.paciente import Paciente
from modules.monticulo_binario import MonticuloBinario
from main import ColaConPrioridad

class TestSalaEmergencias(unittest.TestCase):
    def setUp(self):
        self.cola = ColaConPrioridad()
        self.p1 = Paciente("Ana", 2)
        self.p2 = Paciente("Luis", 1)
        self.p3 = Paciente("Carlos", 3)
        self.p4 = Paciente("Sofía", 1)  # Mismo riesgo que Luis, pero llega después

    def test_orden_prioridad(self):
        self.cola.append(self.p1)
        self.cola.append(self.p2)
        self.cola.append(self.p3)
        self.cola.append(self.p4)

        primero = self.cola.pop()
        segundo = self.cola.pop()

        self.assertEqual(primero.nombre, "Luis")
        self.assertEqual(segundo.nombre, "Sofía")

    def test_len(self):
        self.cola.append(self.p1)
        self.cola.append(self.p2)
        self.assertEqual(len(self.cola), 2)
        self.cola.pop()
        self.assertEqual(len(self.cola), 1)

if __name__ == "__main__":
    unittest.main()
