#1) Imports
from math import sin, cos, pi, sqrt, tan, atan2
#2) Variáveis
x=float(input("Digite o valor de x:"))
y=float(input("Digite o valor de y:"))
#3) Conversão de r
r=sqrt(x**2 + y**2)
#4) Coordenada theta e resultados
if x>0 and y>0:
  theta=atan2(y,x) * (180/pi)
  print ("theta(degree)=", theta)
  print ("r= ", r)
  print ("primeiro quadrante")
elif x<0 and y>0:
  theta=(pi- atan2(y,x)) *(180/pi)
  print ("theta(degree)=", theta)
  print ("r= ", r)
  print ("segundo quadrante")
elif x<0 and y<0:
  theta=(pi +atan2(y,x)) *(180/pi)
  print ("theta(degree)=", theta)
  print ("r= ", r)
  print ("terceiro quadrante")
elif x>0 and y<0:
  theta=(2*pi - atan2(y,x)) * (180/pi)
  print ("theta(degree)=", theta)
  print ("r= ", r)
  print ("quarto quadrante")
