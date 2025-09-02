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

def b2d(b_num):
    return int("".join(str(i) for i in b_num),2)

def evaluar(poblacion):
    # Ordenar de menor a mayor (más óptimos primero, más cerca de 0)
    newP = sorted(poblacion, key=b2d)
    return newP

def seleccionarCompetencia(poblacion: list, fitness_poblacion: list, K: int):
    seleccion_temp = []
    indices_usados = []
    for _ in range(K):
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
    # Seleccionar el genoma más apto como padre (menor fitness)
    padre = min(seleccion_temp, key=lambda x: x[1])[0]
    return padre

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

def recombinar(poblacion: list, p1, p2, p_size, p_binary, combination_rate):
    nueva = []
    if r.random() < combination_rate:
        punto_cruce = r.randint(1, p_binary-1)
        h1 = p1[:punto_cruce] + p2[punto_cruce:]
        h2 = p2[:punto_cruce] + p1[punto_cruce:]
        nueva.append(h1)
        nueva.append(h2)
    poblacion = nueva[:p_size]
    return poblacion

def elitismo(poblacion, fitness, num_elite):
    individuos = []
    elite_indices = [0] * len(poblacion)
    elite_indices.sort(key=lambda x: fitness[x])
    elite_indices = elite_indices[:num_elite]

    for i in elite_indices:
        individuos.append(poblacion[i])
    return individuos

if __name__ == "__main__":
    t = 0
    p_size = 7
    p_binary = 4
    generations = 5
    p_mut = 0.02
    num_elite = 2  # Número de individuos élite a conservar
    combination_rate = 0.8

    p_inicial = np.random.randint(2, size=(p_size, p_binary)).tolist()
    p_inicial = evaluar(p_inicial)

    while t < generations:
        t += 1
        fitness = [int(b2d(ind) ** 2) for ind in p_inicial]

        # Elitismo: conservar los mejores individuos (más cercanos a 0)
        elite = elitismo(p_inicial, fitness, num_elite)

        # Selección y recombinación para el resto de la población
        hijos = []
        while len(hijos) < (p_size - num_elite):
            p1 = seleccionarCompetencia(p_inicial, fitness, K=3)
            p2 = seleccionarCompetencia(p_inicial, fitness, K=3)
            # Recombinación usando la función recombinar
            hijos_parciales = recombinar([], p1, p2, 2, p_binary, combination_rate)
            for h in hijos_parciales:
                if len(hijos) < (p_size - num_elite):
                    hijos.append(h)

        # Mutación
        hijos = mutacion(hijos, p_mut)

        # Nueva población: élite + hijos
        p_inicial = elite + hijos
        p_inicial = evaluar(p_inicial)
        fitness = [int(b2d(ind) ** 2) for ind in p_inicial]

        print(f"Generacion {t}: ")
        for x in p_inicial:
            print(x)

        