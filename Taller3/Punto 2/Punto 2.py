# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:51:58 2018

@author: adrian
"""

#f(1)=0, f(2)=0.69, f'(1)=1, f'(2)=0.5

def diferenciasDivididas(x,y):
    size = len(x)
    
    w, h = 5, 4;
    matrix = [[0 for x in range(w)] for y in range(h)] 
    
    for i in range(size):
        matrix[i][0] = x[i]
        matrix[i][1] = y[i]
    
    matrix[0][2] = 1 # f'(1)=1
    matrix[2][2] = 0.5 # f'(2)=0.5
    
    for i in range(1,size-2):
        matrix[i][2] = ( matrix[i][1] -matrix[i+1][1] )/( matrix[i][0] -matrix[i+1][0] )
        
    for i in range(0,size-2):        
        matrix[i][3] = ( matrix[i+1][2] -matrix[i][2] )/( matrix[i+2][0] -matrix[i][0] )
    
    for i in range(0,size-3):    
        matrix[i][4] = ( matrix[i+1][3] -matrix[i][3] )/( matrix[i+3][0] -matrix[i+1][0] )
    
    print("Matriz de diferencias ",matrix,"\n")
    
    def polynom(x): return matrix[0][1] + matrix[0][2]*(x-1) + matrix[0][3]*((x-1)**2)+matrix[0][4]*((x-1)**2)*(x-2)
    
    print("Polinomio es ",matrix[0][1]," + ", matrix[0][2],"(x-1) + ", matrix[0][3],"(x-1)^2 + ",matrix[0][4],"((x-1)^2)(x-2)")
    
    x = numpy.linspace(-15,15,100) # 100 linearly spaced numbers
    y = polynom(x) # computing the values of sin(x)/x
    
    # compose plot
    pylab.plot(x,y) # sin(x)/x
    pylab.show() # show the plot
    

if __name__ == "__main__":
    x = [1,1,2,2]
    y = [0,0,0.69,0.69]
    diferenciasDivididas(x,y)