# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:08:38 2018

@author: adrian
"""

from random import randint

def printM(M):
	for i in range(len(M)):
		S=str()
		for j in range(len(M[i])):                       
			if(j>len(M)-1):
				S=S+" "+str(M[i][j])
			else:
				S=S+" "+str(int(M[i][j]))
		print(S)

for n in range(2,6):
	r=0
	print("\nn:"+str(n))
	print()
	M=[]
	for i in range(n):
	    V=[]
	    for j in range (n+1):
	        V.append(randint(0,100))
	    M.append(V)
	
	printM(M)
	print(" ")
    
	for i in range(len(M)):#todas las filas
	    p=M[i][i]                
	    for j in range(len(M[i])):               
	        M[i][j]/=p
	        r+=1
	    for j in range(len(M)):#todas las filas
	        if(j!=i):
	            p=M[j][i]
	            for k in range(len(M[j])):#todas las columnas
	                M[j][k]-=p*M[i][k]
	                r+=1

	printM(M)
	print(" ")
	print("r:")
	print(r)