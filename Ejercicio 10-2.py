import tkinter
from tkinter import ttk
import sys

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="Escoge tu favorito para ganar la Champions:")
label_saludo.pack()

lista = ['Real Madrid', 'Bayern Munich', 'Liverpool', 'PSG', 'Chelsea', 'Inter', 'Roma']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)

listbox.pack( anchor= tkinter.W )

window.mainloop()
sys.exit(0)
