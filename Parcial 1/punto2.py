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

#n es número de términos y x es valor a evaluar
def evaluarTaylor(n,valorEvaluacion): 
    func = str(taylor(f,0,n))
    x = valorEvaluacion
    return eval(func)

def aitken(x0,x1,x2,valorEvaluacion,E):        
    err = 1
    j = 3
    i = 1
    print("\t      Término \t     Iteración \t Error relativo")
    a0 = x2-((x2-x1)**2)/(x2-2*x1+x0) #fórmula
    print("\t",a0,"\t                ",i)
    while(err >= E):
        a1 = a0        
        x0 = evaluarTaylor(j-2,valorEvaluacion)
        x1 = evaluarTaylor(j-1,valorEvaluacion)
        x2 = evaluarTaylor(j,valorEvaluacion)        
        a0 = x2-((x2-x1)**2)/(x2-2*x1+x0) #fórmula
        err = (abs(a0-a1)/abs(a0))
        j += 1
        i += 1
        print("\t",a0,"\t",i,"\t",err)

#func = str(taylor(f,0,5))
#print("Términos de la serie tomados: ",func)

valorEvaluacion = 1

x0 = evaluarTaylor(0,valorEvaluacion)
x1 = evaluarTaylor(1,valorEvaluacion)
x2 = evaluarTaylor(2,valorEvaluacion)

E = 1.e-15

aitken(x0, x1, x2, valorEvaluacion,E)

    