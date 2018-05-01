# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:53:04 2018

@author: adrian
"""

from tkinter import Tk, Label, Button, Entry
import modelo
import pylab as plt

class MyGUI:
    
    def __init__(self, master):
        
        self.master = master
        master.title("Simulador potencial de acción en una neurona")

        self.main_label = Label(master, text="Simulador del potencial de acción en una neurona")
        
        self.label_parametros = Label(master, text="Parámetros")
        
        self.label_vacio1 = Label(master, text="")
        self.label_vacio2 = Label(master, text="        ")
        self.label_vacio3 = Label(master, text="")
        self.label_vacio4 = Label(master, text="        ")
        self.label_vacio5 = Label(master, text="        ")
        
        self.label_capacitancia = Label(master, text="Capacitancia membrana (uF/cm^2)")
        self.label_conductanciaNa = Label(master, text="Conductancia gNa (mS/cm^2)")
        self.label_conductanciaK = Label(master, text="Conductancia gK (mS/cm^2)")
        self.label_conductanciaL = Label(master, text="Conductancia gL (mS/cm^2)")
        self.label_potencialNa = Label(master, text="Potencial ENa (mV)")
        self.label_potencialK = Label(master, text="Potencial EK (mV)")
        self.label_potencialL = Label(master, text="Potencial EL (mV)")
      
        self.txt_capacitancia = Entry(master,width=6)
        self.txt_conductanciaNa = Entry(master,width=6)
        self.txt_conductanciaK  = Entry(master,width=6)
        self.txt_conductanciaL = Entry(master,width=6)
        self.txt_potencialNa = Entry(master,width=6)
        self.txt_potencialK = Entry(master,width=6)
        self.txt_potencialL = Entry(master,width=6)
        
        self.label_ajustes = Label(master, text="Ajustes")
        
        self.label_tiempoInicio = Label(master, text="Tiempo inicio (ms)")
        self.label_tiempoFin = Label(master, text="Tiempo fin (ms)")
        self.label_corrienteEntrada = Label(master, text="Corriente de entrada (uA/cm^2)")

        self.txt_tiempoInicio = Entry(master,width=6)
        self.txt_tiempoFin = Entry(master,width=6)
        self.txt_corrienteEntrada  = Entry(master,width=6)
        
        self.simular_button = Button(master, text="      Simular      ", command=self.simular)
        self.parametrosDefault_button = Button(master, text="Establecer parámetros predeterminados", command=self.establecerPPredeterminados)
        self.ajustesDefault_button = Button(master, text="Establecer ajustes predeterminados", command=self.establecerAPredeterminados)
        self.limpiar_button = Button(master, text="Limpiar", command=self.limpiar)
        self.ayuda_button = Button(master, text="Ayuda", command=self.ayudar)
        
        #Ingresar componentes dentro del grid
        
        self.main_label.grid(row=0, columnspan=7)
        
        self.label_vacio1.grid(row=1, columnspan=7)
        self.label_vacio2.grid(column=0, rowspan=11)
        self.label_vacio3.grid(row=3, columnspan=7)
        self.label_vacio4.grid(column=3, rowspan=11)
        self.label_vacio5.grid(column=6, rowspan=11)
        
        self.label_parametros.grid(row=2, column=1, columnspan=2)
        
        self.label_capacitancia.grid(row=4, column=1)
        self.label_conductanciaNa.grid(row=5, column=1)
        self.label_conductanciaK.grid(row=6, column=1)
        self.label_conductanciaL.grid(row=7, column=1)
        self.label_potencialNa.grid(row=8, column=1)
        self.label_potencialK.grid(row=9, column=1)
        self.label_potencialL.grid(row=10, column=1)
        
        self.txt_capacitancia.grid(column=2, row=4)
        self.txt_conductanciaNa.grid(column=2, row=5)
        self.txt_conductanciaK.grid(column=2, row=6)
        self.txt_conductanciaL.grid(column=2, row=7)
        self.txt_potencialNa.grid(column=2, row=8)
        self.txt_potencialK.grid(column=2, row=9)
        self.txt_potencialL.grid(column=2, row=10)
        
        self.label_ajustes.grid(row=2, column=4, columnspan=2)
        
        self.label_tiempoInicio.grid(row=4, column=4)
        self.label_tiempoFin.grid(row=5, column=4)
        self.label_corrienteEntrada.grid(row=6, column=4)
       
        self.txt_tiempoInicio.grid(row=4, column=5)
        self.txt_tiempoFin.grid(row=5, column=5)
        self.txt_corrienteEntrada.grid(row=6, column=5)
        
        self.simular_button.grid(row=9, column=4, columnspan=2)
        self.limpiar_button.grid(row=11, column=4, sticky='W' )
        self.ayuda_button.grid(row=11, column=5)   
        self.parametrosDefault_button.grid(row=11, column=1, columnspan=2) 
        self.ajustesDefault_button.grid(row=7, column=4, columnspan=2)

    def simular(self):
        
        V, m, h, n, t = modelo.resolverModeloHodgkinHuxley(1.0, 120.0, 36.0, 0.3, 50.0, -77.0, -54.387, 0.0, 100.0, 6.5)
        
        plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.title('Hodgkin-Huxley Neuron')
        plt.plot(t, V, 'k')
        plt.ylabel('V (mV)')
        plt.xlabel('t (ms)')
        
        plt.show()
        
        plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(t, m, 'r', label='m')
        plt.plot(t, h, 'g', label='h')
        plt.plot(t, n, 'b', label='n')
        plt.ylabel('Gating Value')
        plt.xlabel('t (ms)')
        plt.legend()
        
        plt.show()

        
    def establecerPPredeterminados(self):
        self.txt_capacitancia.delete(0,'end')
        self.txt_capacitancia.insert(0,1.0)
        self.txt_conductanciaNa.delete(0,'end')
        self.txt_conductanciaNa.insert(0,120.0)
        self.txt_conductanciaK.delete(0,'end')
        self.txt_conductanciaK.insert(0,36.0)
        self.txt_conductanciaL.delete(0,'end')
        self.txt_conductanciaL.insert(0,0.3)
        self.txt_potencialNa.delete(0,'end')
        self.txt_potencialNa.insert(0,50.0)
        self.txt_potencialK.delete(0,'end')
        self.txt_potencialK.insert(0,-77.0)
        self.txt_potencialL.delete(0,'end')
        self.txt_potencialL.insert(0,-54.387)
        
    def establecerAPredeterminados(self):        
        self.txt_tiempoInicio.delete(0,'end')
        self.txt_tiempoInicio.insert(0,0) 
        self.txt_tiempoFin.delete(0,'end')
        self.txt_tiempoFin.insert(0,400.0) 
        self.txt_corrienteEntrada.delete(0,'end')
        self.txt_corrienteEntrada.insert(0,10.0)
    
    def limpiar(self):        
        self.txt_capacitancia.delete(0,'end')
        self.txt_conductanciaNa.delete(0,'end')
        self.txt_conductanciaK.delete(0,'end')
        self.txt_conductanciaL.delete(0,'end')
        self.txt_potencialNa.delete(0,'end')
        self.txt_potencialK.delete(0,'end')
        self.txt_potencialL.delete(0,'end')        
        self.txt_tiempoInicio.delete(0,'end')
        self.txt_tiempoFin.delete(0,'end')
        self.txt_corrienteEntrada.delete(0,'end')
        
    def ayudar(self):
        print("ayudando")

def main():
    root = Tk()
    my_gui = MyGUI(root)
    root.mainloop()    

if __name__ == "__main__":
    main()