#1) Imports
from math import sin, cos, pi, sqrt, tan, atan2
#2) Função
def Catalan(n):
  if n==0:
    return 1
  elif n<=0:
    return ("n deve ser >= 0")
  else:
    return ((4*n - 2)/(n + 1)) * Catalan(n - 1)
#3) Teste
print(Catalan(5))
