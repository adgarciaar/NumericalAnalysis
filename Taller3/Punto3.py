# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 00:49:10 2018

@author: Juanda
"""

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    Input
      datax: input x's in a list of size n
      datay: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
    return p[0]
    
def main():
    x= symbols('x', real=True)
    datx=[0,0.1,0.2,0.3,0.4]
    daty=[0,0.00467884,0.01752309,0.03693637,0.06155793]
    t = np.arange(0, 1, 0.1)
    y=[]
    for i in range(len(t)):
        y.append((neville(datx,daty,t[i])))
    plt.plot(t, y,'bo')
    plt.show()
    poly=neville(datx,daty,0.25)
    
    print('%0.7f'%N(poly))   
if __name__ == "__main__":
    main()