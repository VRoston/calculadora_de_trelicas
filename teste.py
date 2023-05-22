import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Calculo Treliças")
root.minsize(900, 900)
## caixa de entrada de dados
label = tk.Label(root, text="Primeira entrada:")
label.grid(column=0, row=0)
entrada_nos = tk.Entry(root, width=10)
entrada_nos.grid(column=1, row=0)

label2 = tk.Label(root, text="Segunda entrada:")
label2.grid(column=0, row=1)
entrada_vigas = tk.Entry(root, width=10)
entrada_vigas.grid(column=1, row=1)

botão_soma = tk.Button(root, text="Somar", command=lambda: somar_entradas())
botão_soma.grid(column=0, row=2)

def somar_entradas():
    entrada_nos_int = int(entrada_nos.get())
    entrada_vigas_int = int(entrada_vigas.get())
    resultado = entrada_nos_int + entrada_vigas_int
    label3 = tk.Label(root, text=str(resultado))
    label3.grid(column="0", row="4")
    return

root.mainloop()
