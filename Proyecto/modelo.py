# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:16:10 2018

@author: adrian
"""

import scipy as sp
import pylab as plt
from scipy.integrate import odeint

# Constants
#C_m  =   1.0 # membrane capacitance, in uF/cm^2
#g_Na = 120.0 # maximum conducances, in mS/cm^2
#g_K  =  36.0
#g_L  =   0.3
#E_Na =  50.0 # Nernst reversal potentials, in mV
#E_K  = -77.0
#E_L  = -54.387

class modeloHodgkinHuxley:
    
    def __init__(self, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI):
        self.C_m = C_m
        self.g_Na = g_Na
        self.g_K = g_K
        self.g_L = g_L
        self.E_Na = g_Na
        self.E_K = E_K
        self.E_L = E_L
        self.tI = tI
        self.tF = tF
        self.cI = cI
        self.t = sp.arange(tI, tF, 0.1)  # The time to integrate over
        self.V = None
        self.m = None
        self.h = None
        self.n = None
        self.ina = None
        self.ik = None
        self.il = None

    # Channel gating kinetics
    
    # Functions of membrane voltage
    def alpha_m(self, V): 
        return 0.1*(V+40.0)/(1.0 - sp.exp(-(V+40.0) / 10.0))
    def beta_m(self, V):  
        return 4.0*sp.exp(-(V+65.0) / 18.0)
    def alpha_h(self, V): 
        return 0.07*sp.exp(-(V+65.0) / 20.0)
    def beta_h(self, V):  
        return 1.0/(1.0 + sp.exp(-(V+35.0) / 10.0))
    def alpha_n(self, V): 
        return 0.01*(V+55.0)/(1.0 - sp.exp(-(V+55.0) / 10.0))
    def beta_n(self, V):  
        return 0.125*sp.exp(-(V+65) / 80.0)
    
    # Membrane currents (in uA/cm^2)
        
    #  Sodium (Na = element name)
    def I_Na(self, V,m,h):
        return self.g_Na * m**3 * h * (V - self.E_Na)
    #  Potassium (K = element name)
    def I_K(self, V, n):  
        return self.g_K * n**4 * (V - self.E_K)
    #  Leak
    def I_L(self, V):     
        return self.g_L * (V - self.E_L)
    
    # External current
    def I_inj(self, t): 
        return self.cI
    
    # Integrate
    def ecuacionesGenerales(self, X, t):
        V, m, h, n = X
        
        #calculate membrane potential & activation variables
        self.dVdt = (self.I_inj(t) - self.I_Na(V, m, h) - self.I_K(V, n) - self.I_L(V)) / self.C_m
        self.dmdt = self.alpha_m(V)*(1.0-m) - self.beta_m(V)*m
        self.dhdt = self.alpha_h(V)*(1.0-h) - self.beta_h(V)*h
        self.dndt = self.alpha_n(V)*(1.0-n) - self.beta_n(V)*n
        return self.dVdt, self.dmdt, self.dhdt, self.dndt
    
    def resolver(self):    
        X = odeint(self.ecuacionesGenerales, [-65, 0.05, 0.6, 0.32], self.t)
        self.V = X[:,0]
        self.m = X[:,1]
        self.h = X[:,2]
        self.n = X[:,3]
        self.ina = self.I_Na(self.V, self.m, self.h)
        self.ik = self.I_K(self.V, self.n)
        self.il = self.I_L(self.V)

    def graficarPotencial(self):       
        
        plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.title('Hodgkin-Huxley Neuron')
        plt.plot(self.t, self.V, 'k')
        plt.ylabel('V (mV)')
        plt.xlabel('t (ms)')
        
        plt.show()
        
    def graficarSegundo(self):    
        
        plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(self.t, self.ina, 'c', label='$I_{Na}$')
        plt.plot(self.t, self.ik, 'y', label='$I_{K}$')
        plt.plot(self.t, self.il, 'm', label='$I_{L}$')
        plt.ylabel('Current')
        plt.xlabel('t (ms)')
        plt.legend()
        
        plt.show()
        
    def graficarActivacionCanales(self):    
        
        plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(self.t, self.m, 'r', label='m')
        plt.plot(self.t, self.h, 'g', label='h')
        plt.plot(self.t, self.n, 'b', label='n')
        plt.ylabel('Gating Value')
        plt.xlabel('t (ms)')
        plt.legend()
        
        plt.show()
        
        #z = []
        #for x in range(0,1000):
        #    z.append(I_inj(x))
        
        #plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        #plt.plot(t, z, 'k')
        #plt.xlabel('t (ms)')
        #plt.ylabel('$I_{inj}$ ($\\mu{F}/cm^2$)')
        #plt.ylim(-1, 31)
        
        #plt.show()
    
modelo = modeloHodgkinHuxley(1.0, 120.0, 36.0, 0.3, 50.0, -77.0, -54.387, 0.0, 400.0, 10)
modelo.resolver()
modelo.graficarPotencial()