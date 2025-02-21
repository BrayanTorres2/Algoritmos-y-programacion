"""
Entradas:
DatoA-->int-->A
DatoB-->int-->B
DatoC-->int-->C
DatoD-->int-->D
Salidas:
Ecuacion1-->float-->ec1
Ecuacion2-->float-->ec2
"""
A=int(input("Ingresar valor de A: "))
B=int(input("Ingresar el valor de B: "))
C=int(input("Ingresar el valor de C: "))
D=int(input("Ingresar el valor de D: "))
ec1=(A-C)**2
if(D<=0):
    print("El resultado es: "+str(ec1))
else:
    ec2=((A-B)**3)/D
    print("El resultado es: "+str(ec2))

    