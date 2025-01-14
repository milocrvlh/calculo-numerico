"""
Esse código serviu para determinar o erro do p_1(x) e p_2(x), para uma primeira tentativa de entender o processo
do algoritmo para depois automátizá-lo para tornar fácil encontrar o k mais adequado ao problema.
"""

import numpy as np

# Definindo o domínio das funções
x = np.linspace(-1, 1, 100)

# Quadratura de Gauss-Legendre
def quadgl(f, n):
    abscissa, coeficiente = np.polynomial.legendre.leggauss(n)
    aproximacao = sum(coeficiente * f(abscissa))
    return aproximacao

## Cálculo do erro
# Definição das funções erro
def err_1(x):
    return (np.exp(-x)/(np.sqrt(x*x+np.exp(-x)) + x) - (-1.414135*x+1.193016))**2
def err_2(x):
    return (np.exp(-x)/(np.sqrt(x*x+np.exp(-x)) + x) - (0.558986*x*x-1.414135*x+1.006687))**2

# Aproximação dos erros para 6 casas após a vírgula
print(f"{quadgl(err_1, 1):.6f}")
print(f"{quadgl(err_2, 1):.6f}")
