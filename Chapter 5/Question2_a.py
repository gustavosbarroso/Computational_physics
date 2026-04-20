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
s=(f(a) + f(b))
for k in range (1,N):
  if k%2==0:
    s+= 2*f(a + k*h)
  else:
    s+= 4*f(a + k*h)
resultado =(h*s)/3
#Resultado
print(resultado)
