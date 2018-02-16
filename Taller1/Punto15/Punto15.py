# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:34:09 2018

@author: adrian
"""

import math
from sympy import *
from sympy.abc import u

fIntegral = 5 - exp(u)
fIzquierda = 2

def f1(limiteInferior,limiteSuperior):
    return integrate(fIntegral, (u, limiteInferior, limiteSuperior))

def f2(x):
    return fIzquierda    

def fx(x):
    limiteInferior = 0
    limiteSuperior = x
    return f1(0,x) - fIzquierda

print("Función es ",fx(x))


#GRÁFICA

from matplotlib import pyplot

# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
pyplot.plot(x, [f1(0,i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)
# Guardar gráfico como imágen PNG.
#pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()


#función equivalente

# x = (1 + exp (x)) / 5 

def g(x):
    return (1 + exp(x)) / 5 

#intervalo entre 0 y 3
    
def puntoFijo(x0, tolerancia, maxIt):
    i = 1
    while(i <= maxIt):
        p = g(x0)
        if(abs(p-x0) < tolerancia):
            return p
        i = i + 1
        x0 = p
    print("Método falló")

print(puntoFijo(0.6,0.1,5))

