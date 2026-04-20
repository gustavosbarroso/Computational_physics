#Import
import numpy as np
import matplotlib.pyplot as plt
#Constantes
g=9.81 #m/s^2
l=0.10 #m
#Sistema de equações
def f(r,t):
  theta=r[0]
  omega=r[1]
  ftheta= omega
  fomega=-(g/l)*np.sin(theta)
  return np.array([ftheta,fomega],float)
#RK4
a = 0.0
b = 10
N = 1000
h = (b - a) / N


tpontos = np.arange(a, b, h)
thetapontos = []
omegapontos = []
#Condição inicial
r=np.array([0.0,np.pi,], float)
#Simulação
for t in tpontos:
    thetapontos.append(r[0])  # salva o valor atual
    omegapontos.append(r[1])  # salva o valor atual
    k1=h * f(r, t)
    k2=h* f(r + 0.5*k1, t+0.5*h)
    k3=h* f(r + 0.5*k2, t+0.5*h)
    k4=h* f(r + k3, t+ h)
    r +=  (k1 + 2*k2 + 2*k3+ k4)/6

#Plots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Gráfico de theta(t)
axs[0].plot(tpontos, thetapontos)
axs[0].set_xlabel("t")
axs[0].set_ylabel("rad")
axs[0].set_title("theta(t)")
axs[0].grid(True)

# Gráfico de omega(t)
axs[1].plot(tpontos, omegapontos)
axs[1].set_xlabel("t")
axs[1].set_ylabel("rad/s")
axs[1].set_title("omega(t)")
axs[1].grid(True)

plt.tight_layout()
plt.show()
