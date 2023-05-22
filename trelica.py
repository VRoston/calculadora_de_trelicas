import tkinter as tk                                    # importa a biblioteca tkinter para usar com a API tk
import numpy as np                                      # importa a biblioteca numpy para usar com a API tk
import matplotlib.pyplot as plt                         # importa a biblioteca matplotlib para usar com a API tk

root = tk.Tk()                                          # cria uma janela

root.title("Calculo Treliças")                          # adiciona um titulo a janela
root.minsize(900, 900)                                  # define o tamanho da janela             
            
# caixa de entrada de dados dos nós 
label = tk.Label (root , text = "Numero de nós:")
label.grid (column = 0, row = 0)
entrada_nos = tk.Entry (root ,width=10)                 # cria uma caixa de entrada do tamanho 10
entrada_nos.grid(column=1, row=0)

# caixa de entrada de dados das barras
label = tk.Label (root , text = "Numero de barras:")
label.grid (column = 0, row = 1)
entrada_vigas = tk.Entry (root ,width=10)               # cria uma caixa de entrada do tamanho 10
entrada_vigas.grid(column=1, row=1)                     # define a localização da caixa 

botão_confirmar = tk.Button(root, text="OK", command=lambda: botão_confirmar()) # usa a função BUtton para criar um botão 
botão_confirmar.grid(column=0, row=2)

def botão_confirmar():
    entrada_nos_int = int(entrada_nos.get())
    entrada_vigas_int = int(entrada_vigas.get())
    
    label3 = tk.Label(root, text=str("sexo"))
    label3.grid(column="0", row="4")
    return


root.mainloop()                                         # deixa o programa aberto