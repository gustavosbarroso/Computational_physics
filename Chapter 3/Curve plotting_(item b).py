#Imports
import numpy as np
import matplotlib.pyplot as plt
#Intervalo de theta
theta=linspace(0,10* np.pi, 1000)
#Função radial
r=theta**2
#Coordenadas cartesianas
x=r*np.cos(theta)
y=r*np.sin(theta)
#Plot
plt.xlabel ("x")
plt.ylabel ("y")
plt.title("Espiral de Galileu")
plt.plot(x,y)
plt.show()
