# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:34:09 2018

@author: adrian
"""

#GRÁFICA

import math
from matplotlib import pyplot
# Función cuadrática.
def f1(x):
    return 5*x - math.exp(x)
# Función lineal.
def f2(x):
    return 1
# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
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