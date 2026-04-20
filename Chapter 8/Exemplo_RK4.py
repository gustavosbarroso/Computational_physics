#Import
import numpy as np
import matplotlib.pyplot as plt
#Função
def f(x,t):
    return -x**3 + np.sin(t)
#RK4
a = 0.0
b = 10
N = 1000
h = (b - a) / N

x = 0.0

tpontos = np.arange(a, b, h)
xpontos = []

for t in tpontos:
    xpontos.append(x)   # salva o valor atual
    k1=h * f(x, t)
    k2=h* f(x + 0.5*k1, t+0.5*h)
    k3=h* f(x + 0.5*k2, t+0.5*h)
    k4=h* f(x + k3, t+ h)
    x +=  (k1 + 2*k2 + 2*k3+ k4)/6

plt.plot(tpontos, xpontos)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Solução de x' = -x³ + sin(t)")
plt.show()
