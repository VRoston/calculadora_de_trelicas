import tkinter as tk                                                 # importa a biblioteca tkinter para usar com a API tk
import numpy as np                                                   # importa a biblioteca numpy para usar com a API tk



root = tk.Tk()                                                       # cria uma janela
# Tamanho Tela
root.title("Calculo Treliças")                                       # adiciona um titulo a janela      
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = int(5*sw/6)
wh = int(5*sh/6)
who = int(1*(sh-wh)/3)
wwo = int((sw-ww)/2)                                                  # define o tamanho da janela     
winsize = str(ww)+'x'+str(wh)+'+'+str(wwo)+'+'+str(who) 
root.geometry(winsize)        






# caixa de entrada de dados dos nós 
label = tk.Label (root , text = "Numero de nós:")
label.grid (column = 0, row = 0)
entrada_nos = tk.Entry (root ,width=10)                              # cria uma caixa de entrada do tamanho 10
entrada_nos.grid(column=1, row=0)

# caixa de entrada de dados das barras
label = tk.Label (root , text = "Numero de barras:")
label.grid (column = 0, row = 1)
entrada_vigas = tk.Entry (root ,width=10)                            # cria uma caixa de entrada do tamanho 10
entrada_vigas.grid(column=1, row=1)                                  # define a localização da caixa 

botão_confirmar = tk.Button(root, text="proximo", command=lambda: botão_confirmar()) # usa a função Button para criar um botão 
botão_confirmar.grid(column=0, row=2)


 
contador_de_linhas = int(4)                                          # cria uma lista para armazenar as barras
cordenadas_das_barras = []                                           # cria uma lista para armazenar as cordenadas das barras

def botão_confirmar():      
    entrada_nos_int = int(entrada_nos.get())                         # transformar a variavel entradanos no tipo INT
    linhas = int (contador_de_linhas) 
    v_posição_x = []                                                     # cria uma lista para armazenar as posições X dos nós  
    v_posição_y = []                                                     # cria uma lista para armazenar as posições Y dos nós 
    entrada_x = ""
    entrada_y = ""                                 
    for i in range(entrada_nos_int):
        linhas = linhas + 1
        label = tk.Label (root , text = "posição X e Y do nó " + str(i+1) + ":")      
        label.grid (column = 0, row =linhas)   

        entrada_x = tk.Entry (root ,width=10)                        # cria uma caixa de entrada do tamanho 10
        entrada_x.grid(column=1, row=linhas) 
        v_posição_x.append(entrada_x)                                 # adiciona as posições X dos nós na lista v_posição_x         
        entrada_y = tk.Entry (root ,width=10)                        # cria uma caixa de entrada do tamanho 10
        entrada_y.grid(column=2, row=linhas)     
        v_posição_y.append(entrada_y)  
                                       
               
    botão_confirmar = tk.Button(root, text="proximo", command=lambda: botão_proximo()) # usa a função Button para criar um botão 
    botão_confirmar.grid(column=0, row=linhas+1)
    
    botão_teste = tk.Button(root, text="teste", command=lambda: teste() ) # usa a função Button para criar um botão 
    botão_teste.grid(column=3, row=linhas+1)
    
    return linhas , v_posição_x , v_posição_y

def teste():
    aleatorio = botão_confirmar()                       # transformar a variavel v_posição_x no tipo INT)
    aleatorio = aleatorio[1]  
    #aleatorio_string = list (map (str, aleatorio))                                  
    for i in range(5):
     print (aleatorio[i])


def botão_proximo():                                                 # Função do botão                
    entrada_vigas_int = int(entrada_vigas.get())                     # transformar as duas varias entradavigas e entradanos no tipo INT   
    linhas = botão_confirmar()                              # transformar a variavel linhas no tipo INT  
    linhas = linhas[0]
    linhas = linhas + 2
    aleatorio = botão_confirmar()                       # transformar a variavel v_posição_x no tipo INT)
    aleatorio = aleatorio[1]                                     
    for i in range(entrada_vigas_int):
        linhas = linhas +1 
        
        result_confirm = tk.Label(text = ("Posicoes salvadas com sucesso" + str(aleatorio)))
        result_confirm.grid(column=0, row=linhas+1, columnspan=3)
        
        label = tk.Label (root , text = "diaga entre quais nós estão a barra" + str(i+1) + ":")      
        label.grid (column = 0, row = linhas)                        # imprimindo mensagem para as barras
        entrada_barras= tk.Entry (root ,width=10)                    # cria uma caixa de entrada do tamanho 10
        entrada_barras.grid(column=1, row=linhas)                    # para receber as cordenadas das barras
        cordenadas_das_barras.append(entrada_barras)                 # adiciona as cordenadas das barras na lista cordenadas_das_barras
        entrada_barras= tk.Entry (root ,width=10)                    # cria uma caixa de entrada do tamanho 10
        entrada_barras.grid(column=2, row=linhas)                    # para receber a segunda cordenada da barra
        cordenadas_das_barras.append(entrada_barras)                 # adiciona as cordenadas das barras na lista cordenadas_das_barras
        
        
    
    return

root.mainloop()                                                      # deixa o programa aberto

# https://github.com/adtzlr/trusspy/blob/main/README.md link para o repositorio de calculadora de treliças
