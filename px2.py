"""
Esse código serviu para determinar o segundo polinômio p_2(x), em que integrais presentes necessitavam
ser resolvidas de forma numérica. Para isso, usei a Quadratura de Gauss-Legendre para uma precisão
de E-6 com apenas 9 pontos. O código também foi usado para minimizar o erro nas demais operações.
"""

import numpy as np

# Definindo o domínio das funções
x = np.linspace(-1, 1, 100)

# Quadratura de Gauss-Legendre
def quadgl(f, n):
    abscissa, coeficiente = np.polynomial.legendre.leggauss(n)
    aproximacao = sum(coeficiente * f(abscissa))
    return aproximacao

## Cálculo da integral para determinar p_2(x)
# Definição da integral
def h(x):
    return (x*x-1/3)*(np.exp(-x)/(np.sqrt(x*x+np.exp(-x)) + x))

# Função do Enunciado
def f(x):
    return np.exp(-x)/(np.sqrt(x*x+np.exp(-x)) + x)

# Aproximação para a função numerador
print(f"{quadgl(h, 9):.6f}")

# Produto
print(f"{quadgl(h, 9)*45/8:.6f}")

# Soma do segundo termo com os outros polinômios
print(f"{quadgl(f, 9)/2-(1/3)*quadgl(h, 9)*45/8:.6f}")

