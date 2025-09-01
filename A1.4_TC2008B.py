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

# Seleccionar individuos por competencia (tournament selection).
def seleccionarCompetencia(poblacion: list, fitness_poblacion: list, k: int):
    seleccion_temp = []     # Selección de genomas aleatorios.
    indices_usados = []     # Índices utilizados (para no repetirse en la aleatoriedad).
    padres = []             # Padres (par de genomas más aptos).

    for p in range(2):
        for i in range(k):
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
        
        padres.append(max(seleccion_temp)[0])   # Seleccionar el genoma más apto como uno de los padres.
        indices_usados = []                     # Reiniciar lista de índices utilizados.

    return padres


# Seleccionar individuos por ruleta.
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

- Huddar, M. [Mahesh Huddar]. (2024, 20 abril). Selection Operators Roulette wheel ranking tournament selection in genetic algorithm Mahesh Huddar [Video]. YouTube. https://www.youtube.com/watch?v=uRF7xSQwNeU
- NeuralNine. (2024, 2 abril). Genetic Algorithms in Python - Evolution for optimization [Video]. YouTube. Recuperado el 30 de agosto de 2025, de https://www.youtube.com/watch?v=CRtZ-APJEKI
"""