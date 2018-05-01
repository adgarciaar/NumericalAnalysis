# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:17:03 2018

@author: adrian
"""

from tkinter import Button, TOP, BOTH, BOTTOM

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

from modelo import resolverModeloHodgkinHuxley

import pylab as plt
import scipy as sp

class GUIgraficas:
    
    def __init__(self, master, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI):
        
        self.master = master
        self.master.title("Gráficas")
        self.cI = cI
        self.V, self.m, self.h, self.n, self.t = resolverModeloHodgkinHuxley(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, tI, tF, cI)

        self.fig = plt.figure(num=None, figsize=(12, 6), dpi=70, facecolor='w', edgecolor='k')
        
        plt.subplot(3,1,1)
        plt.title('Dinámica modelo Hodgkin-Huxley')
        plt.plot(self.t, self.V, 'k')
        plt.ylabel('V (mV)')
        
        plt.subplot(3,1,2)
        plt.plot(self.t, self.m, 'r', label='m')
        plt.plot(self.t, self.h, 'g', label='h')
        plt.plot(self.t, self.n, 'b', label='n')
        plt.ylabel('Valor de activación')
        #plt.xlabel('t (ms)')
        plt.legend()
        
        t = sp.arange(tI, tF, 0.1)
        plt.subplot(3,1,3)
        plt.plot(t, self.I_entrada(t), 'k')
        plt.xlabel('t (ms)')
        plt.ylabel('$I_{inj}$ ($\\mu{F}/cm^2$)')
        plt.ylim(-1, 31)       
        
        plt.close()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, master)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)     
        
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        
        button = Button(master=master, text="Cerrar", command=self.cerrar)
        button.pack(side=BOTTOM)
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)        
        
    def cerrar(self):
        self.master.quit()     # stops mainloop
        self.master.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
    def on_closing(self):
        self.master.quit()     
        self.master.destroy()
        
    def I_entrada(self, t):
        #return self.cI*(t>30) + self.cI*(t>60) + self.cI*(t>90)
        return self.cI*(t>0)