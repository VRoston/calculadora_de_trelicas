import math
import numpy
import tkinter as tk
import customtkinter  as ctk 

#                               Tamanho Da tela
numpy.set_printoptions(3, suppress=True)
root = ctk.CTk()                  # Cria a nossa janela
root._set_appearance_mode('dark') 
root.title('Calculadora de Treliçãs')
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = int(5*sw/6)
wh = int(5*sh/6)
who = int(1*(sh-wh)/3)
wwo = int((sw-ww)/2)
root.minsize(800,600)
winsize = str(ww)+'x'+str(wh)+'+'+str(wwo)+'+'+str(who) 
root.geometry(winsize)

                            # Configuração dos frames
root.columnconfigure([0,1], weight=1)
root.rowconfigure(1, weight=1)
titleframe = ctk.CTkFrame(root,bg_color='#071e26')
guiframe = ctk.CTkFrame(root,bg_color='#071e26') #
graphframe = ctk.CTkFrame(root,bg_color='#071e26')
titleframe.grid(row=0,column=0,columnspan=2,sticky='nsew')
guiframe.grid(row=1,column=0,sticky='nsew')
graphframe.grid(row=1,column=1,sticky='nsew')

titleframe.columnconfigure(0, weight=1)
titlelbl = ctk.CTkLabel(titleframe, text='Calculadora de Treliças 2d',bg_color='#071e26',text_color='white')
titlelbl.grid(row=0,column=0,sticky='nsew')

guiframe.columnconfigure(0, weight=1)
guiframe.rowconfigure(0, weight=1)
guiframe.grid_propagate(0)

guicanvs = ctk.CTkCanvas(guiframe, highlightthickness=0,background='#071e26',)
guivscrol = ctk.CTkScrollbar(guiframe, orientation='vertical', command=guicanvs.yview,)  #scrollbar esquerda
guihscrol = ctk.CTkScrollbar(guiframe, orientation='horizontal', command=guicanvs.xview,) #scrollbar direita
guicanvs.grid(row=0,column=0,sticky='nsew')
guivscrol.grid(row=0,column=1,rowspan=2,sticky='nsew')
guihscrol.grid(row=1,column=0,sticky='nsew')

guicanvs.columnconfigure(0, weight=1)
guicanvs.rowconfigure(0, weight=1)
containerframe = ctk.CTkFrame(guicanvs,fg_color='#071e26')
containerframe.grid(row=0,column=0,sticky='nsew')

guicanvs.create_window((0,0), width=ww/2-17, window=containerframe, anchor='nw', tags=('canwin'))

containerframe.bind('<Configure>', lambda e: guicanvs.configure(scrollregion=guicanvs.bbox('all')))
guicanvs.configure(yscrollcommand=guivscrol.set, xscrollcommand=guihscrol.set)

containerframe.columnconfigure([0,1,2], weight=1)

graphframe.grid_propagate(0)
graphframe.columnconfigure(0, weight=1)
graphframe.rowconfigure(0, weight=1)
plotcanvs = ctk.CTkCanvas(graphframe,highlightthickness=0, width=ww/2,)
plotcanvs.grid(row=0,column=0,sticky='nsew')


v_posição_x = []
v_posição_x.clear()
v_posição_y = []
v_posição_y.clear()



# caixa de entrada de dados dos nós 
label = ctk.CTkLabel (containerframe , text = "Numero de nós:",text_color='white',)
label.grid (column = 0, row = 0)
entrada_nos = ctk.CTkEntry (containerframe ,width=100,border_color='#071e26')                              # cria uma caixa de entrada do tamanho 10
entrada_nos.grid(column=1, row=0)

# caixa de entrada de dados das barras
label = ctk.CTkLabel(containerframe , text = "Numero de barras:",text_color='white')
label.grid (column = 0, row = 1)
entrada_vigas = ctk.CTkEntry (containerframe,width=100,border_color='#071e26')                            # cria uma caixa de entrada do tamanho 10
entrada_vigas.grid(column=1, row=1)            

botão_confirmar = ctk.CTkButton(containerframe, text="proximo", command=lambda: botão_confirmar()) # usa a função Button para criar um botão 
botão_confirmar.grid(column=0, row=2)

lista_de_entradanos_x = []                                             # cria uma lista para armazenar os nós
lista_de_entradanos_y = []                                             # cria uma lista para armazenar os nós
contador_de_linhas = int(4)                                          # cria uma lista para armazenar as barras
cordenadas_das_barras = []                                           # cria uma lista para armazenar as cordenadas das barras
def botão_confirmar():      
    entrada_nos_int = int(entrada_nos.get())                         # transformar a variavel entradanos no tipo INT
    linhas = int (contador_de_linhas) 
    #global v_posição_x                                                 # cria uma lista para armazenar as posições X dos nós  
    #global v_posição_y                                                 # cria uma lista para armazenar as posições Y dos nós 
    
                                 
    for i in range(entrada_nos_int):
        linhas = linhas + 1
        label = ctk.CTkLabel (containerframe , text = "posição X e Y do nó " + str(i+1) + ":",text_color='white')      
        label.grid (column = 0, row =linhas)   
        
        caixa = ctk.CTkEntry (containerframe,width=100,border_color='#071e26')                              # cria uma caixa de entrada do tamanho 10
        caixa.grid(column=1, row=linhas)
        lista_de_entradanos_x.append(caixa) # adiciona as posições X dos nós na lista de entrada de nós
            
                                        # adiciona as posições X dos nós na lista v_posiçãok_
        caixa = ctk.CTkEntry (containerframe ,width=100,border_color='#071e26')                              # cria uma caixa de entrada do tamanho 10
        caixa.grid(column=2, row=linhas)
        lista_de_entradanos_y.append(caixa) 
                                       
               
    botão_confirmar = ctk.CTkButton(containerframe, text="proximo", command=lambda: botão_proximo()) # usa a função Button para criar um botão 
    botão_confirmar.grid(column=0, row=linhas+1)
    
    #botão_teste = ctk.CTkButton(containerframe, text="teste", command=lambda: teste() ) # usa a função Button para criar um botão 
   # botão_teste.grid(column=3, row=linhas+1)
    
    return linhas , v_posição_x , v_posição_y

def teste():
    global v_posição_x                                                 # cria uma lista para armazenar as posições X dos nós  
    global v_posição_y 
    tamanho_lista = len(lista_de_entradanos_x) #len é uma função que pega o tamanho da lista 
    print (lista_de_entradanos_x)
    for i in range(tamanho_lista):
        #print (v_posição_x[i])
        v_posição_x.append(int(lista_de_entradanos_x[i].get()))      # esse funciona para pegar o valor da caixa de entrada
        v_posição_y.append(int(lista_de_entradanos_y[i].get()))      # esse funciona para pegar o valor da caixa de entrada
        print (v_posição_x[i])
        print (v_posição_y[i])


def botão_proximo():                                                 # Função do botão                
    entrada_vigas_int = int(entrada_vigas.get())                     # transformar as duas varias entradavigas e entradanos no tipo INT   
    linhas = botão_confirmar()                              # transformar a variavel linhas no tipo INT  
    linhas = linhas[0]
    linhas = linhas + 2
    aleatorio = botão_confirmar()                       # transformar a variavel v_posição_x no tipo INT)
    aleatorio = aleatorio[1]                                     
    for i in range(entrada_vigas_int):
        linhas = linhas +1 
        
        #result_confirm = ctk.CTkLabel(containerframe,text = ("Posicoes salvadas com sucesso" + str(aleatorio)))
        #result_confirm.grid(column=0, row=linhas+1, columnspan=3)
        
        label = ctk.CTkLabel (containerframe , text = "diga entre quais nós estão a barra " + str(i+1) + ":",text_color='white')      
        label.grid (column = 0, row = linhas)                        # imprimindo mensagem para as barras
        entrada_barras= ctk.CTkEntry (containerframe,width=100,border_color='#071e26')                    # cria uma caixa de entrada do tamanho 100
        entrada_barras.grid(column=1, row=linhas)                    # para receber as cordenadas das barras
        cordenadas_das_barras.append(entrada_barras)                 # adiciona as cordenadas das barras na lista cordenadas_das_barras
        entrada_barras= ctk.CTkEntry (containerframe ,width=100,border_color='#071e26')                    # cria uma caixa de entrada do tamanho 100
        entrada_barras.grid(column=2, row=linhas)                    # para receber a segunda cordenada da barra
        cordenadas_das_barras.append(entrada_barras)                 # adiciona as cordenadas das barras na lista cordenadas_das_barras
        
        
    
    return

root.mainloop() # Fim da janela