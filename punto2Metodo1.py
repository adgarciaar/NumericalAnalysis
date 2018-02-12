# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:29:29 2018

@author: adrian
"""

from numpy import sign

def busquedaIncremental(f,a,b,intervalo,error):
    
    x1 = a
    x2 = a + intervalo
    f1 = f(a) 
    f2 = f(x2)   
    
    while (sign(f1) == sign(f2) and abs(x2-x1)>=error):
        if (x2 >= b): 
            return None
        else:        
            x1 = x2 
            x2 = x1 + intervalo
            f1 = f2
            f2 = f(x2)
        
    return (x1 + x2)/2.0
    
    
def f(x): return 4.0*x**3 - 112.0*x**2 + 768.0*x - 1000

largo = 32
ancho = 24
intervalo = 0.0001
error = 0.00000001
maximo = ancho/2 - intervalo
contador = 0

raices = []       

while (contador < maximo):
    
    a = contador
    b = contador + intervalo    
    resultado = busquedaIncremental(f,a,b,intervalo,error)  
    
    if (resultado != None):
        raices.append(resultado)
    contador += intervalo

print (raices)