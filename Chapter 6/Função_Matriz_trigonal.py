from numpy import empty, zeros
from pylab import plot, show

def matrizTrigonal(N, C, m, k, omega):
    alfa = 2*k - m*omega**2

    # Matriz
    A = zeros([N, N], float)

    for i in range(N):
        A[i, i] = alfa
        if i < N-1:
            A[i, i+1] = -k
            A[i+1, i] = -k

    # Ajuste das bordas
    A[0,0] = alfa - k
    A[N-1,N-1] = alfa - k

    # Vetor
    v = zeros(N, float)
    v[0] = C

    # Eliminação de Gauss
    for i in range(N-1):
        fator = A[i+1, i] / A[i, i]
        A[i+1, i+1] -= fator * A[i, i+1]
        v[i+1] -= fator * v[i]

    # Substituição regressiva
    x = empty(N, float)
    x[N-1] = v[N-1] / A[N-1, N-1]

    for i in range(N-2, -1, -1):
        x[i] = (v[i] - A[i, i+1] * x[i+1]) / A[i, i]

    return x


# Chamada
x = matrizTrigonal(26, 1, 1, 6, 2)

# Plot
plot(x)
plot(x, "k.")
show()
