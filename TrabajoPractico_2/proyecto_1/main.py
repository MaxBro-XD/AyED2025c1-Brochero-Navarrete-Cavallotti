"""
Sala de emergencias
"""

import time
import datetime
import random
import modules.paciente as pac
from modules.cola_prioridad import ColaConPrioridad

n = 20  # cantidad de ciclos de simulación

cola_de_espera = ColaConPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente por segundo
    paciente = pac.Paciente()
    cola_de_espera.append(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and len(cola_de_espera) > 0:
        paciente_atendido = cola_de_espera.pop()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)