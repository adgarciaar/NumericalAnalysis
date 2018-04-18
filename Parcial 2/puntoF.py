# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 07:30:49 2018

@author: adrian
"""

# Regla de Simpson 1/3

import math
from scipy.optimize import fsolve
from numpy import sign
from numpy import exp
 
# Función f(x)
def f(x):
    return 4+math.cos(x+1)

# Función g(x)
def g(x):
    return (math.exp(x))*(math.sin(x))
 
# Función para aproximación de la integral
def simpson( limInf, limSup, nParticiones, funcion ):
 
    # Cálculo del valor de h
    h = ( limSup - limInf )/nParticiones
 
    # List for storing value of x and f(x)
    x = list()
    fx = list()
     
    # Calcular valores de x y f(x)
    i = 0
    while i<= nParticiones:
        x.append(limInf + i * h)
        fx.append(funcion(x[i]))
        i += 1
 
    # Cálculo del resultado
    res = 0
    i = 0
    while i<= nParticiones:
        if i == 0 or i == nParticiones:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res

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

def resta(x): return f(x) - g(x)

def encontrarRaices():
    intervalo = 0.0001
    error = 0.000001
    maximo = 5
    contador = -5
    
    raices = []       
    
    while (contador < maximo):
        
        a = contador
        b = contador + intervalo    
        resultado = busquedaIncremental(resta,a,b,intervalo,error)  
        
        if (resultado != None):
            raices.append(resultado)
        contador += intervalo
        
    print("\nPuntos de intersección de las dos curvas: \n",raices,"\n")
    return raices

def main():
    
    raices = encontrarRaices()
    
    limInferior = raices[0]
    limSuperior = raices[1]
    
    puntoMedio = (limSuperior + limInferior)/2
        
    if(f(puntoMedio) > g(puntoMedio)):
        fMayor = f
        fMenor = g
    else:
        fMayor = g
        fMenor = f
     
    nParticiones = 10
    
    simpsonMayor = simpson(limInferior, limSuperior, nParticiones, fMayor)
    simpsonMenor = simpson(limInferior, limSuperior, nParticiones, fMenor)
    
    resultado = simpsonMayor - simpsonMenor
    print('Área encerrada por las curvas entre x=',limInferior,' y x=',limSuperior,' es ',resultado,' unidades cuadradas (u^2)')

if __name__ == "__main__":
    main()