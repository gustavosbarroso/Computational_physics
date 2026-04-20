from math import pi, sqrt

# Entrada
l1 = float(input("Distância no periélio (l1) = "))
v1 = float(input("Velocidade no periélio (v1) = "))

# Constante gravitacional do Sol (GM) em unidades astronômicas
GM = 4 * pi**2

# Semi-eixo maior (via energia orbital)
a = 1 / ((2 / l1) - (v1**2 / GM))

# Afélio (l2)
l2 = 2*a - l1

# Semi-eixo menor
b = sqrt(l1 * l2)

# Velocidade no afélio
v2 = (l1 * v1) / l2

# Período orbital
T = (2 * pi * a * b) / (l1 * v1)

# Excentricidade
e = (l2 - l1) / (l2 + l1)

# Saída
print("l2 (UA)=", l2)
print("v2 (UA/ano)=", v2)
print("T (anos)=", T)
print("e =", e)
