# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:53:04 2018

@author: adrian
"""

from tkinter import Tk, Label, Button
from tkinter import LEFT, RIGHT

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
        
        self.simular_button = Button(master, text="Simular", command=self.simular)
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
        #self.close_button.pack(side=RIGHT)
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
        
        self.simular_button.grid(row=8, column=4, columnspan=2)
        self.limpiar_button.grid(row=9, column=4, columnspan=2)
        self.ayuda_button.grid(row=10, column=4, columnspan=2)       

    def simular(self):
        print("Simulando")
        
    def limpiar(self):
        print("limpiando")
        
    def ayudar(self):
        print("ayudando")

def main():
    root = Tk()
    my_gui = MyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()