# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:44:20 2018

@author: adrian
"""

from numpy import sign

def calcularRaiz(f,a,b,error):
    
    f1 = f(a)
    d = (b-a)/10
    x = a + d    
    f2 = f(x)
    
    while(d>error):
        while (sign(f1) == sign(f2)):
            x = x + d
            f1 = f2
            f2 = f(x)
            if(sign(f1) != sign(f2)):     
                x = x-d
                d = d/10                
                f2 = f(x)   
    
    print(x)
    
    
def f(x): return 4.0*x**3 - 112.0*x**2 + 768.0*x - 1000

calcularRaiz(f,1,2,0.01)
