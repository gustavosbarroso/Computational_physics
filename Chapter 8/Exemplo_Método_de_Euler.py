#Import
import numpy as np
import matplotlib.pyplot as plt
#Função
def f(x,t):
    return -x**3 + np.sin(t)
#Método de Euler
a = 0.0
b = 10
N = 1000
h = (b - a) / N

x = 0.0

tpontos = np.arange(a, b, h)
xpontos = []

for t in tpontos:
    xpontos.append(x)   # salva o valor atual
    x += h * f(x, t)
#Plot
plt.plot(tpontos, xpontos)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Solução de x' = -x³ + sin(t)")
plt.show()
