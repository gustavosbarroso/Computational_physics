import numpy as np
import matplotlib.pyplot as plt

# Função (EDO) (exemplo)
def f(x, t):
    return -x**3 + np.sin(t)

# RK4
def RK4simples(f, a, b, N, x0):
    h = (b - a) / N
    tpontos = np.arange(a, b, h)

    xpontos = []
    x = x0

    for t in tpontos:
        xpontos.append(x)

        k1 = h * f(x, t)
        k2 = h * f(x + 0.5*k1, t + 0.5*h)
        k3 = h * f(x + 0.5*k2, t + 0.5*h)
        k4 = h * f(x + k3, t + h)

        x += (k1 + 2*k2 + 2*k3 + k4) / 6

    return tpontos, xpontos

# Chamada
tpontos, xpontos = RK4simples(f, 0, 10, 1000, 0.0)

# Plot
plt.plot(tpontos, xpontos)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Solução de x' = -x³ + sin(t) (RK4)")
plt.show()
