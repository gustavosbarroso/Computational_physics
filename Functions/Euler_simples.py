#Import
import numpy as np
import matplotlib.pyplot as plt
#Função
def f(x,t):
    return -x**3 + np.sin(t)
#Método de Euler
def Euler(f, a, b, N, x0):
  h = (b - a) / N

  tpontos = np.arange(a, b, h)
  xpontos = []
  x=x0

  for t in tpontos:
      xpontos.append(x)   # salva o valor atual
      x += h * f(x, t)
  return tpontos, xpontos
#Chamada da função
tpontos, xpontos=Euler(f, 0, 10, 1000, 0.0)
#Plot
plt.plot(tpontos, xpontos)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Solução de x' = -x³ + sin(t)")
plt.show()
