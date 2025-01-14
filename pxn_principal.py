"""
Esse código resolve o problema por completo, garantindo uma precisão de 10^(-6).
"""
from sympy.integrals.quadrature import gauss_legendre
from sympy import *

# Quadratura de Gauss-Legendre
def quadgl(expressao, nos):
    soma = 0
    abscissas, constantes = gauss_legendre(nos, 11)
    for abscissa, constante in zip(abscissas, constantes):
        soma += constante * expressao.evalf(subs={x: abscissa})
    return soma
    

# Declarando a incógnita x
x = symbols('x')

f = exp(-x)/(sqrt(x**2+exp(-x)) + x)

# Processo baseado no algoritmo de Gram-Schmidt para a ortogonalização
def B(k):
    if k == 1:
        return integrate(x * (phi(0))**2, (x, -1, 1))/ integrate((phi(0))**2, (x, -1, 1))
    elif k >= 2:
        return integrate(x * (phi(k-1))**2, (x, -1, 1))/ integrate((phi(k-1))**2, (x, -1, 1))

def C(k):
    if k >= 2:
        return integrate(x * (phi(k-1))*(phi(k-2)), (x, -1, 1))/ integrate((phi(k-2))**2, (x, -1, 1))

def phi(k):
    if k == 0:
        return 1
    elif k == 1:
        return x - B(1)
    elif k >= 2:
       return (x - B(k))*phi(k-1) - C(k)*phi(k-2)
    
# Determinar o coeficiente
def a(k):
    return quadgl(phi(k)*f, 11) / integrate(phi(k)**2, (x, -1, 1))

# Determinar o polinômio
def p(k):
    polinomio = 0
    for i in range(k+1):
        polinomio += phi(i)*a(i)
    return simplify(polinomio)

# Determinar o erro da aproximação pelo polinômio
def erro(k):
    return quadgl((f-p(k))**2, 11) 

# Determina e exibe os polinômios, erros e seleciona o polinômio com k ideal
def melhor_aproximacao():
    k = 0
    while True:
        err = erro(k)
        print(f"Para k = {k}, o polinômio é {p(k).evalf(6)}, com erro de {err:.7f}.")
        if err < 10**(-6):
            print(f"Essa é a melhor aproximação com precisão de 10^(-6)!")
            break
        k +=1
# Inicia o programa
if __name__ == "__main__":
    melhor_aproximacao()
