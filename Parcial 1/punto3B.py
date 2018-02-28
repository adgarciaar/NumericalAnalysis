#Punto 3 b)

from math import *
from sympy import *

gx="log(x+2)-sin(x)" 
g1x=str(diff(gx))
g2x=str(diff(g1x))

def NewtonGeneralizado(x,tolerancia,N):
    i = 1
    print("Iteración \t\t g(f(x)) \t\t Error\n")
    while i<=N:
        d= float(eval(g1x))
        if d != 0:
            x0= x - (((eval(gx)*d))/((d**2)-eval(gx)*eval(g2x)))
        error = (abs(x0-x) / abs(x0))
        print(i,"\t\t",x0,"\t",error);
        if error<tolerancia:
            print("\nLa raiz es ",x0)            
            break
        i=i+1
        x=x0
    if i>=N:
        print("El método no converge ")
        
NewtonGeneralizado(-1.8, 1.e-5,20)