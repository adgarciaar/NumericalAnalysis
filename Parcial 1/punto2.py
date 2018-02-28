# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:13:49 2018

@author: adrian
"""

import math
import sympy as sy

# Define the variable and the function to approximate
x = sy.Symbol('x')
f = sy.exp(x)

# Taylor approximation at x0 of the function 'function'
def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(math.factorial(i))*(x-x0)**i
        i += 1
    return p

def aitken(p0, tol, maxIt):
    b = 0
    i=1
    while(i<=maxIt):
        p1 = taylor(f,p0)
        p2 = taylor(f,p1)
        p = p0 - ((p1-p0)**2)/(p2-2*p1+p0)
        
        if(abs(p-p0)<tol):
            print ("Solución aproximada es ",p)
            b = 1
            break
        i += 1
        p0 = p
    
    if(b == 0):
        print("Método falló luego de ",maxIt)
        
func = str(taylor(f,0,5))
print("Términos de la serie tomados: ",func)

x = 1
print("Evaluación cuando x = ",x," es ",eval(func))
    
#aitken(0.0, 0.00001, 1000)

    