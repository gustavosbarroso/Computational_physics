# Imports
from numpy import empty, zeros
from pylab import plot, show

# Constantes
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0

alfa = 2*k - m*omega**2

# Matriz inicial
A = zeros([N, N], float)

for i in range(N-1):
    A[i, i] = alfa
    A[i, i+1] = -k
    A[i+1, i] = -k

A[N-1, N-1] = alfa
A[0,0] = alfa - k
A[N-1,N-1] = alfa - k

# Vetor
v = zeros(N, float)
v[0] = C

# Eliminação gaussiana
for i in range(N-1):
    fator = A[i+1, i] / A[i, i]
    A[i+1, i+1] -= fator * A[i, i+1]
    v[i+1] -= fator * v[i]
    A[i+1, i] = 0  # limpa a subdiagonal

# Substituição regressiva
x = empty(N, float)
x[N-1] = v[N-1] / A[N-1, N-1]

for i in range(N-2, -1, -1):
    x[i] = (v[i] - A[i, i+1]*x[i+1]) / A[i, i]

# Plot
plot(x)
plot(x, "k.")
show()
