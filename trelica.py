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

botão_confirmar = tk.Button(root, text="OK", command=lambda: botão_confirmar()) # usa a função Button para criar um botão 
botão_confirmar.grid(column=0, row=2)

def botão_confirmar():                                  # Função do botão 
    entrada_nos_int = int(entrada_nos.get())                 
    entrada_vigas_int = int(entrada_vigas.get())        # transformar as duas varias entradavigas e entradanos no tipo INT
    linhas = 4                                          # váriavel auxiliar para imprimir texto 
    int (linhas)
    
    for i in range(entrada_nos_int):
        linhas = linhas + 1
        label = tk.Label (root , text = "posição X do nó " + str(i+1) + ":")      
        label.grid (column = 0, row = linhas)                       # Impressão do texto da posição X
        entrada_vigas_int = tk.Entry (root ,width=10)               # cria uma caixa de entrada do tamanho 10
        entrada_vigas_int.grid(column=1, row=linhas)  
    
        label = tk.Label (root , text = "posição Y do nó " + str(i+1) + ":")
        label.grid (column = 0, row = linhas+1)
        entrada_vigas_int2 = tk.Entry (root ,width=10)               # cria uma caixa de entrada do tamanho 10
        entrada_vigas_int2.grid(column=1, row=linhas+1)  
        
    return


root.mainloop()                                         # deixa o programa aberto