import math
from scipy import integrate
import numpy as np


# Define a função que você deseja integrar
def f(x):
    return x / (np.tan(x))


# Calcule a integral da função f(x) de 0 a infinito (np.inf)
resposta, error = integrate.quad(f, 0, np.pi / 2)

print(math.factorial(5))  # fatorial
print(math.pow(5, 2))  # elevado
print(math.log(23, 2))  # log
print(math.ceil(234.23))  # arrendonda pra cima
print(math.floor(234.23))  # inteiro mais baixo proximo

print()
# Imprima o resultado da integral e a estimativa de erro
print("O valor da integral é:", resposta)
print("O erro estimado é:", error)
