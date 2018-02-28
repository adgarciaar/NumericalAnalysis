#Punto 3 b)

from math import *
from sympy import *

gx="log(x+2)-sin(x)" 
g1x=str(diff(gx))
g2x=str(diff(g1x))

def main(x,tolerancia,N,i):

    print('iteracion\tg(f(x))\t\terror\t\tderivada')
    while i<=N:
        d= float(eval(g1x))
        if d != 0:
            x0= x - (((eval(gx)*d))/((d**2)-eval(gx)*eval(g2x)))
        er=abs(x0-x)
        print("%d\t\t%.5f\t\t%.5f\t\t%.5f"%(i,x0,er,d));
        if er<tolerancia:
            print("La raiz es %.6f"%x0)            
            break
        i=i+1
        x=x0
    if i>=N:
        print("El método no converge ")
        
main(-1.8, 0.00001,20,1)