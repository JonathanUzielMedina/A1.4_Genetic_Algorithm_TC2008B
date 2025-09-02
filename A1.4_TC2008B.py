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

#alternativamente sin numpy
#p_inicial2 = [[r.randint(0,1) for _ in range(p_binary)] for _ in range(p_size)]

def b2d(b_num):
    return int("".join(str(i) for i in b_num),2)

def evaluar(poblacion):
    newP = sorted(poblacion, key=b2d, reverse=False)
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

def recombinar(poblacion: list, p1, p2, p_size):
    nueva = []
    for i in range(p_size // 2):
        punto_cruce = r.randint(1, p_binary-1)
        h1 = p1[:punto_cruce] + p2[punto_cruce:]
        h2 = p2[:punto_cruce] + p1[punto_cruce:]
        nueva.append(h1)
        nueva.append(h2)
    poblacion = nueva[:p_size]
    return poblacion

if __name__ == "__main__":
    t = 0
    p_size = 7
    p_binary = 4
    generations = 8
    p_mut = 0.08
    p_inicial = np.random.randint(2,size= (p_size,p_binary))
    
    evaluar(p_inicial)
    fitness = [] # Valores de aptitud de los genomas
    for g in range(len(p_inicial)):
        fitness.append(int(b2d(p_inicial[g]) ** 2))
        
    parada = False
    while t < generations:
        t += 1
        p1 = seleccionarRuleta(p_inicial, fitness)
        p2 = seleccionarRuleta(p_inicial, fitness)
        '''felipe arregla tu funcion'''
        #p_inicial = recombinar(p_inicial, p1, p2, p_size)
        p_inicial = mutacion(p_inicial, p_mut)
        evaluar(p_inicial)
        
        for g in range(len(p_inicial)):
            fitness.append(int(b2d(p_inicial[g]) ** 2))
        
        print(f"Generacion {t}: ")
        for x in p_inicial:
            print(x)

        
        