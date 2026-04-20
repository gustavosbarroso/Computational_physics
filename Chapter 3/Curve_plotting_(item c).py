#Imports
import numpy as np
import matplotlib.pyplot as plt
#Intervalo de theta
theta=linspace(0,24* np.pi, 1000)
#Função radial
r=np.exp(np.cos(theta))-2*np.cos(4*theta)+(np.sin(theta/12))**5
#Coordenadas cartesianas
x=r*np.cos(theta)
y=r*np.sin(theta)
#Plot
plt.xlabel ("x")
plt.ylabel ("y")
plt.title("Função de Fey")
plt.plot(x,y)
plt.show()
