# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:13:49 2018

@author: adrian
"""

def f(x): return exp(x)

def aitken(p0, tol, maxIt):
    b = 0
    i=1
    while(i<=maxIt):
        p1 = f(p0)
        p2 = f(p1)
        p = p0 - ((p1-p0)**2)/(p2-2*p1+p0)
        
        if(abs(p-p0)<tol):
            print ("Solución aproximada es ",p)
            b = 1
            break
        i+= 1
        p0 = p
    
    if(b == 0):
        print("Método falló luego de ",maxIt)
    
aitken(1.0, 0.01, 1000)
    