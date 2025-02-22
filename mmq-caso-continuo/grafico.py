"""
Esse código contempla o gráfico que precisei fazer para ter ideia do comportamento da função.
"""

from numpy import *
import matplotlib.pyplot as plt

# Permitir usar Latex
plt.rcParams['text.usetex'] = True

# Definindo domínio e função
x = linspace(-1, 1, 100)

y = sqrt(x**2 + exp(-x)) - x
y0 = 1.19302 * ones_like(x)
y1 = 1.19302 - 1.41414*x
y2 = 0.558986*x**2 - 1.41414*x + 1.00669
y3 = 0.107004*x**3 + 0.558986*x**2 - 1.47834*x + 1.00669
y4 = -0.0767541*x**4 + 0.107004*x**3 + 0.624775*x**2 - 1.47834*x + 1.00011
y5 = -0.0740307*x**5 - 0.0767541*x**4 + 0.18926*x**3 + 0.624775*x**2 - 1.49596*x + 1.00011

# Faz o gráfico
plt.plot(x, y, label=r"$f(x)=\sqrt{x^2 + e^{-x}} - x$")
plt.plot(x, y0, label=r"$p_0(x)$")
plt.plot(x, y1, label=r"$p_1(x)$")
plt.plot(x, y2, label=r"$p_2(x)$")
plt.plot(x, y3, label=r"$p_3(x)$")
plt.plot(x, y4, label=r"$p_4(x)$")
plt.plot(x, y5, label=r"$p_5(x)$")

plt.title(r"$f(x)=\sqrt{x^2 + e^{-x}} - x$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.grid(True)
plt.savefig('mmq-caso-continuo/grafico.png')
plt.show()
