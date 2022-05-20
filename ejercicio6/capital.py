"""Programa NO. 6
para calcular para calcular en cuantos meses se duplica un capital dado"""

#output

C = int(input("Digite el valor de c: "))
D= 2*C
N=0

#processing 
while C < D:
    C=C+(0.05)*C
    N=N+1
print("En "+str(N)+ " meses la capital tendra el un valor de: " +str(C))
