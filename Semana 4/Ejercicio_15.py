"""
Entradas
edad->int->edad
hemoglobina->float->h
sexo->str->sexo
Salidas
anemia->str->anemina
"""
#entradas
edad=int(input("Ingrese la edad: "))
h=float(input("Ingrese nivel de hemoglobina: "))
sexo=input("Ingrese su sexo F=Femenino, M=Masculino: ")
anemia=""
#Caja negra
if(edad>0 and edad<=1 and h<13 and h>=26):
    anemia="posivo"
elif(edad>1 and edad<=6 and h<10 and h>=18):
    anemia="posivo" 
elif(edad>6 and edad<=12 and h<11 and h>=15):
    anemia="posivo"       
print(anemia)    