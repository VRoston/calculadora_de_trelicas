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

posição_x = []                                          # cria uma lista para armazenar as posições X dos nós
posição_y = []                                          # cria uma lista para armazenar as posições Y dos nós
contador_de_linhas = 4                                  # váriavel auxiliar para imprimir texto 
                                          

def botão_confirmar():                                  # Função do botão 
    entrada_nos_int = int(entrada_nos.get())            # transformar a variavel entradanos no tipo INT
    linhas = int (contador_de_linhas)                                        # transformar a variavel linhas no tipo INT
    
    for i in range(entrada_nos_int):
        linhas = linhas + 1
        label = tk.Label (root , text = "posição X e Y do nó " + str(i+1) + ":")      
        label.grid (column = 0, row = linhas)            # Impressão do texto da posição X
        posição_x = tk.Entry (root ,width=10)            # cria uma caixa de entrada do tamanho 10
        posição_x.grid(column=1, row=linhas)             # para a posição X do nó 
        posição_y = tk.Entry (root ,width=10)            # cria uma caixa de entrada do tamanho 10
        posição_y.grid(column=2, row=linhas)             # para a posição Y do nó
        
        
    botão_confirmar = tk.Button(root, text="proximo", command=lambda: botão_proximo()) # usa a função Button para criar um botão 
    botão_confirmar.grid(column=0, row=linhas+1)
    return
def botão_proximo():                                     # Função do botão 
    entrada_nos_int = int(entrada_nos.get())                 
    entrada_vigas_int = int(entrada_vigas.get())         # transformar as duas varias entradavigas e entradanos no tipo INT                                          # váriavel auxiliar para imprimir texto 
    linhas = int (contador_de_linhas) 
    
    for i in range(entrada_vigas_int):
        linhas = linhas + 1
        label = tk.Label (root , text = "posição X e Y do nó " + str(i+1) + ":")      
        label.grid (column = 0, row = linhas)            # Impressão do texto da posição X
        posição_x = tk.Entry (root ,width=10)            # cria uma caixa de entrada do tamanho 10
        posição_x.grid(column=1, row=linhas)             # para a posição X do nó 
        posição_y = tk.Entry (root ,width=10)            # cria uma caixa de entrada do tamanho 10
        posição_y.grid(column=2, row=linhas)             # para a posição Y do nó
    
    return

root.mainloop()                                          # deixa o programa aberto