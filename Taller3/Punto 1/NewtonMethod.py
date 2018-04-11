# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:30:04 2018

@author: Juanda
"""
## module newtonPoly
''' p = evalPoly(a,xData,x).
Evaluates Newton’s polynomial p at x. The coefficient
vector {a} can be computed by the function ’coeffts’.
a = coeffts(xData,yData).
Computes the coefficients of Newton’s polynomial.
'''
import numpy as np
from numpy import *

def _poly_newton_coefficient(x,y):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(x[k:m] - x[k-1])

    return a

def newton_polynomial(x_data, y_data, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -x_data[n-k])*p
    return p

x = [0,1,2]
y = [10,15,5]
a=_poly_newton_coefficient(x,y)
print("Coeficientes del polinomio" , a)
