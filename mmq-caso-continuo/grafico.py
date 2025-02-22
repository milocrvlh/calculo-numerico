"""
Esse código contempla o gráfico que precisei fazer para ter ideia do comportamento da função.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definindo o domínio das funções
x = np.linspace(-1, 1, 100)

# Permitir usar Latex
plt.rcParams['text.usetex'] = True

# Definindo domínio e função
x = np.linspace(-1, 1, 100)
y = np.exp(-x) / (np.sqrt(x**2+np.exp(-x)) + x)

# Faz o gráfico
plt.plot(x, y, color = 'blue', linewidth='2')
plt.title(r"$f(x)=\frac{e^{-x}}{\sqrt{x^2 + e^{-x}} + x}$")


plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
