"""
A1.4 Genetic Algorithms (GAs)

Modelación de Sistemas Multiagentes y Gráficas Computacionales (TC2008B).

Equipo:
    - Jesús Felipe Bastidas Valenzuela (A01255206)
    - Sebastián Blachet Sánchez (A00227588)
    - Eduardo Cárdenas Valadez (A002332432)
    - Jonathan Uziel Medina Rodríguez (A01255048)
    - Araceli Ruiz Sánchez (A01255302)

Docente: Dr. Edgar León Sandoval.

Fecha de entrega: 1 de septiembre de 2025.
________________________________________________________________________
Descripción: Implementación del algoritmo genético.
"""

import numpy as np
import random as r

# x es cualquier numero dentro de 15, por lo que en binario ocupa 4 bits 
p_size = 7
p_binary = 4

p_inicial = np.random.randint(2,size= (p_size,p_binary))

#alternativamente sin numpy
p_inicial2 = [[r.randint(0,1) for _ in range(p_binary)] for _ in range(p_size)]



def inicializar(t: int):
    pass

def seleccionar(t: int):
    pass

def evaluar(t: int):
    pass
    
def mutacion(poblacion, prob):
    newP = []
    for parte in poblacion:
        newparte = []
        for bit in parte:
            if r.random() < prob:
                newparte.append(1 - bit) 
            else:
                newparte.append(bit)
        newP.append(newparte)
    return newP

def recombinar(t: int):
    pass

if __name__ == "__main__":
  t = 0
  parada = False
  while not parada:
      t += 1


"""
Referencias:

- Huddar, M. [Mahesh Huddar]. (2024, 20 abril). Selection Operators Roulette wheel ranking tournament selection in genetic algorithm Mahesh Huddar [Video]. YouTube. Recuperado el 30 de agosto de 2025, de https://www.youtube.com/watch?v=uRF7xSQwNeU
- NeuralNine. (2024, 2 abril). Genetic Algorithms in Python - Evolution for optimization [Video]. YouTube. Recuperado el 30 de agosto de 2025, de https://www.youtube.com/watch?v=CRtZ-APJEKI
"""
