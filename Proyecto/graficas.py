import modelo

from six.moves import tkinter as Tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

import pylab as plt

V, m, h, n, z = modelo.resolverModeloHodgkinHuxley(1.0, 120.0, 36.0, 0.3, 50.0, -77.0, -54.387, 0.0, 100.0, 5.6)

root = Tk.Tk()
root.wm_title("Embedding in Tk")

#fig = Figure(figsize=(5, 4), dpi=100)
#t = np.arange(0, 100.0, .1)
#fig.add_subplot(111).plot(t, V)

V, m, h, n, t = modelo.resolverModeloHodgkinHuxley(1.0, 120.0, 36.0, 0.3, 50.0, -77.0, -54.387, 0.0, 100.0, 6.5)
     
fig = plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')

plt.subplot(2,1,1)
plt.title('Hodgkin-Huxley Neuron')
plt.plot(t, V, 'k')
plt.ylabel('V (mV)')

plt.subplot(2,1,2)
plt.plot(t, m, 'r', label='m')
plt.plot(t, h, 'g', label='h')
plt.plot(t, n, 'b', label='n')
plt.ylabel('Gating Value')
plt.xlabel('t (ms)')
plt.legend()
plt.close()

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = Tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.