# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 08:26:36 2018

@author: Juanda
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 08:10:38 2018

@author: Juanda
"""
import numpy as np
def funcion(z):
    return (1/(2*np.pi)**1/2)*np.exp(-1/2*z**2)
def trapecios(f,a,b,n):
    m=(b-a)*n
    h=(b-a)/m
    s=0
    for i in range(1,m):
        s=s+f(a+i*h)
    r=h/2*(f(a)+2*s+f(b))
    return r
a=trapecios(funcion,-2,2,10**4)
print(a)