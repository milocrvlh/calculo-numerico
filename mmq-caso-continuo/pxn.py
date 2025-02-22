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
        # Para [-1, 0]
        soma += (1/2) * constante * expressao.evalf(subs={x: (1/2)*(abscissa - 1)}) 

        # Para [0, 1]
        soma += (1/2) * constante * expressao.evalf(subs={x: (1/2)*(abscissa + 1)})
    return soma


# Declarando a incógnita x
x = symbols('x')

# A implementação correta do erro de f(x)
f_positiva = exp(-x)/(sqrt(x**2+exp(-x)) + x)
f_negativa = sqrt(x**2+exp(-x)) - x
f = Piecewise(
    (f_positiva, 0 <= x),
    (f_negativa, x < 0)
)

# Processo baseado no algoritmo de Gram-Schmidt para a ortogonalização
def B(k):
    phi_0 = phi(0)
    phi_k1 = phi(k-1)
    if k == 1:
        return integrate(x * (phi_0)**2, (x, -1, 1))/ integrate((phi_0)**2, (x, -1, 1))
    elif k >= 2:
        return integrate(x * (phi_k1)**2, (x, -1, 1))/ integrate((phi_k1)**2, (x, -1, 1))

def C(k):
    phi_k2 = phi(k-2) 
    if k >= 2:
        return integrate(x * (phi(k-1))*(phi_k2), (x, -1, 1))/ integrate((phi_k2)**2, (x, -1, 1))

def phi(k):
    if k == 0:
        return 1
    elif k == 1:
        return x - B(1)
    elif k >= 2:
       return (x - B(k))*phi(k-1) - C(k)*phi(k-2)
    
# Determinar o coeficiente
def a(k):
    phi_k = phi(k)
    return quadgl(phi_k*f, 11)/ integrate(phi_k**2, (x, -1, 1))

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
