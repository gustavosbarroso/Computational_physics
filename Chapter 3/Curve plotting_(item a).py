#import
from pylab import plot,show, xlabel, ylabel, title
from numpy import linspace,sin, sqrt,pi, cos
#intervalo de theta
theta=linspace(0,2*pi,1000)
#função deltoide
x = 2*cos(theta) + cos(2*theta)
y = 2*sin(theta) -sin (2*theta)
#plot
xlabel ("x")
ylabel ("y")
title("Deltoide")
plot(x,y)
show()
