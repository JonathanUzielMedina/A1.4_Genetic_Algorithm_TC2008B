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

def b2d(b_num):
    return int("".join(str(i) for i in b_num), 2)

def evaluar(poblacion):
    newP = sorted(poblacion, key=b2d, reverse=True)
    return newP

# Seleccionar un individuo por competencia (tournament selection).
def seleccionarCompetencia(poblacion: list, fitness_poblacion: list, K: int):
    seleccion_temp = []     # Selección de genomas aleatorios.
    indices_usados = []     # Índices utilizados (para no repetirse en la aleatoriedad).

    for i in range(K):
        idx = r.randint(0, len(poblacion)-1)
        if idx not in indices_usados:
            seleccion_temp.append((poblacion[idx], fitness_poblacion[idx]))
            indices_usados.append(idx)
        else:
            while idx in indices_usados:
                idx = r.randint(0, len(poblacion)-1)
                if idx not in indices_usados:
                    seleccion_temp.append((poblacion[idx], fitness_poblacion[idx]))
                    indices_usados.append(idx)
                    break
    padre = max(seleccion_temp)[0]  # Seleccionar el genoma más apto como padre.
    return padre


# Seleccionar un individuo por ruleta.
def seleccionarRuleta(poblacion: list, fitness_poblacion: list):
    sumaFitness = sum(fitness_poblacion)
    numeroRandom = int(r.randint(0, sumaFitness))
    actual = 0

    for i in range(len(poblacion)):
        actual += fitness_poblacion[i]
        if actual > numeroRandom:
            return poblacion[i]


def mutacion(t: int):
    pass

def recombinar(t: int):
    pass

if __name__ == "__main__":
    print(f"\nPoblación inicial:\n\n{p_inicial2}\n")

    fitness = [] # Valores de aptitud de los genomas

    for g in range(len(p_inicial2)):
        fitness.append(int(b2d(p_inicial2[g]) ** 2))
    
    print(f"\nSelección por competencia:\n\n{seleccionarCompetencia(p_inicial2, fitness, 3)}\n")
    
    print(f"\nSelección por ruleta:\n\n{seleccionarRuleta(p_inicial2, fitness)}\n")
    
    """
    t = 0
    parada = False
    while not parada:
        t += 1
    """

"""
Referencias:

- Huddar, M. [Mahesh Huddar]. (2024, 20 abril). Selection Operators Roulette wheel ranking tournament selection in genetic algorithm Mahesh Huddar [Video]. YouTube. Recuperado el 30 de agosto de 2025, de https://www.youtube.com/watch?v=uRF7xSQwNeU
- NeuralNine. (2024, 2 abril). Genetic Algorithms in Python - Evolution for optimization [Video]. YouTube. Recuperado el 30 de agosto de 2025, de https://www.youtube.com/watch?v=CRtZ-APJEKI
"""