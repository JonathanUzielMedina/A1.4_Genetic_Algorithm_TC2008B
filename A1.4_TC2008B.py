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

def mutacion(t: int):
    pass

def recombinar(t: int):
    pass

if __name__ == "__main__":
  t = 0
  parada = False
  while not parada:
      t += 1