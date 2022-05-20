"""Programa NO. 1
para calcular la suma de los N primeros números enteros"""

print("--------------------------------------------------")
print("-------------suma de primeros enesimos------------")
print("--------------------------------------------------")

#input 

n=int(input("digite el valor de n: "))
resultado=0
cant_num=0

#processing 

while cant_num<n:
    cant_num+1
    resultado=resultado+cant_num

#output
print(" la suma de los primero" + str(n) + " nuḿeros naturales es igual a " + str(resultado))

