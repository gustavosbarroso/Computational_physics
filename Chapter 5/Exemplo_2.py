#Imports
import numpy as np
import matplotlib.pyplot as plt
#Função
def f(x):
  return x**4 - 2*x + 1
#Integração
a=0.0
b=2.0
N=100
h=(b-a)/N
s=0.5*(f(a) + f(b))
for k in range (1,N):
  s+= f(a+ k*h)
#Resultado
print(h*s)
