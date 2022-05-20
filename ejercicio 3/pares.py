"""Programa NO. 2
para calcular el rango de números enteros, obtener la
cantidad de números que contiene una cifra"""

#input 

a= int(input("Digite el valor de a:"))
b= int(input("Digite el valor de b:"))

#processing

if (a <b):
    cant_num=0
    a=a+1
    while (a <b):
        cant_num=cant_num+1
        r=a%2
        if(r==0):
            cant_num=cant_num +1
        a=a+1
    print(cant_num)
else:
    print("a debe ser menor que b")




