datos=input()
x,y=datos.split(" ")
x=float(x)
y=float(y)
if(x==0 and y==0):
    print("Origem")
elif(x==0):
    print("Eixo x")
elif(y==0):
    print("Eixo y") 
elif(x>0 and y>0):
    print("Q1")
elif(x<0 and y>0):
    print("Q2")
elif(x>0 and y<0):
    print("Q4")  
elif(x<0 and y<0):
    print("Q3")                            