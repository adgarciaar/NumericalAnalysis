# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:03:20 2018

@author: adrian
"""

#GRÁFICAS 

#función r=2+cos(3t)

import numpy as np 
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi)
r = 2+ np.cos(3*theta)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(5)
ax.grid(True)

ax.set_title("Función r=2+cos(3t)", va='bottom')

plt.show()


#función r=2-e^t, duda con la gráfica respecto a Wolfram

theta = np.linspace(-np.pi,2*np.pi/3)
r = 2 - np.exp(theta)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(5)
ax.grid(True)

ax.set_title("Función r=2-e^t", va='bottom')

plt.show()


#RAÍCES

from numpy import sign
from numpy import exp

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

    
def f(x): return exp(x) - cos(3*x)

intervalo = 0.0001
error = 0.000001
maximo = 2*np.pi
contador = -2*np.pi

raices = []       

while (contador < maximo):
    
    a = contador
    b = contador + intervalo    
    resultado = busquedaIncremental(f,a,b,intervalo,error)  
    
    if (resultado != None):
        raices.append(resultado)
    contador += intervalo
    
print("\nRaices: \n",raices,"\n")
