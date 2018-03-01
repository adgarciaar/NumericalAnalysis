# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:45:23 2018

@author: adrian
"""

import numpy as np

def f(x): return np.log(x+2) - np.sin(x)
def f1x(x): return (1/(x+2)) - np.cos(x)

def secante(x0,x1):     
  
  x = (f(x1)*x0-f(x0)*x1)/(f(x1)-f(x0))
  error = 1 
  
  while (error > 1.e-7):      
    x0 = x1
    x1 = x
    x = (f(x1)*x0-f(x0)*x1)/(f(x1)-f(x0))
    if (f(x) == 0):
        break
    error = abs(f(x)/f1x(x))
    print("x = ",x,"\t","E = ",error)
  
secante(-1.8,-1.0)