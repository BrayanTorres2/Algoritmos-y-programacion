n=input()
(a,b,c,d)=n.split(" ")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if d==0:
    print((a-c)**2)
elif d>0:
    print(((a-b)**3)/d)