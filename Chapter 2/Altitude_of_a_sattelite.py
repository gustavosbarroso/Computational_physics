#1)Constantes
G=6.67 * 10**-11 #(N * m^2)/kg^2
M=5.97 * 10**24 #kg
R=6.371 * 10**6 #m
#2)Valor da altura
T=float(input("T= ")) #em segundos
#3) Altura
h=(((G*M*T**2)/(4 * (3.14)**2))**(1/3) - R)
#4) Impressão da altura
print("h=", f": {(h/1000):.2f}", "km")
