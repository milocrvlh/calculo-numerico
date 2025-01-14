"""
Esse código serviu para determinar o primeiro polinômio p_1(x), em que integrais presentes necessitavam
ser resolvidas de forma numérica. Para isso, usei a Quadratura de Gauss-Legendre para uma precisão
de E-6 com apenas 9 pontos. O código também foi usado para minimizar o erro nas operações para determinar os coeficientes
"""

import numpy as np

# Definindo o domínio das funções
x = np.linspace(-1, 1, 100)

# Quadratura de Gauss-Legendre
def quadgl(f, n):
    abscissa, coeficiente = np.polynomial.legendre.leggauss(n)
    aproximacao = sum(coeficiente * f(abscissa))
    return aproximacao

## Cálculo das Integrais para determinar p_1(x)
# Definição das integrais
def f(x):
    return np.exp(-x)/(np.sqrt(x*x+np.exp(-x)) + x)

def g(x):
    return (x * np.exp(-x))/(np.sqrt(x*x+np.exp(-x)) + x)

# Aproximação para as funções
print(f"{quadgl(f, 9):.6f}")
print(f"{quadgl(g, 9):.6f}")

# Resultado dos coeficientes
print(f"{quadgl(f, 9)/2:.6f}")
print(f"{quadgl(g, 9)*3/2:.6f}")



