import matplotlib.pyplot as plt
import numpy as np
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
def RK4(f, a, b, N, r):

    h = (b - a) / N
    tpontos = np.linspace(a, b, N+1)
    r = np.array(r, float)

    thetapontos = [r[0]]
    omegapontos=[r[1]]

    for i in range(N):
        t=tpontos[i]

        k1 = h * f(r, t)
        k2 = h * f(r + 0.5*k1, t + 0.5*h)
        k3 = h * f(r + 0.5*k2, t + 0.5*h)
        k4 = h * f(r + k3, t + h)

        r=r+  (k1 + 2*k2 + 2*k3 + k4) / 6

        thetapontos.append(r[0])
        omegapontos.append(r[1])

    return tpontos, thetapontos, omegapontos

#Chamada da função
tpontos, thetapontos, omegapontos=RK4(f, 0, 10, 1000, [0.0, np.pi])
#Plots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Gráfico de theta(t)
axs[0].plot(tpontos, thetapontos)
axs[0].set_xlabel("s")
axs[0].set_ylabel("rad")
axs[0].set_title("theta(t)")
axs[0].grid(True)

# Gráfico de omega(t)
axs[1].plot(tpontos, omegapontos)
axs[1].set_xlabel("s")
axs[1].set_ylabel("rad/s")
axs[1].set_title("omega(t)")
axs[1].grid(True)

plt.tight_layout()
plt.show()
