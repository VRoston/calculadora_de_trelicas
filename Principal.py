import math
import numpy
import tkinter as tk
import customtkinter  as ctk 
import string
                                   # Tamanho Da tela
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
titleframe = ctk.CTkFrame(root,bg_color='#030e11')  # Frame do Titulo
guiframe = ctk.CTkFrame(root,bg_color='#030e11')    # Frame Principal
graphframe = ctk.CTkFrame(root,bg_color='#030e11')  # Frame Grafíco
titleframe.grid(row=0,column=0,columnspan=2,sticky='nsew')
guiframe.grid(row=1,column=0,sticky='nsew')
graphframe.grid(row=1,column=1,sticky='nsew')

                            # Frame Do Título
titleframe.columnconfigure(0, weight=1)
titlelbl = ctk.CTkLabel(titleframe, text='Calculadora de Treliças 2d',bg_color='#020a0d',text_color='white')
titlelbl.grid(row=0,column=0,sticky='nsew')

                            # Frame Principal
guiframe.columnconfigure(0, weight=1)
guiframe.rowconfigure(0, weight=1)
guiframe.grid_propagate(0)

guicanvs = ctk.CTkCanvas(guiframe, highlightthickness=0,background='#030e11',)                             
guivscrol = ctk.CTkScrollbar(guiframe, orientation='vertical', command=guicanvs.yview,bg_color='#030e11')  #scrollbar esquerda
guihscrol = ctk.CTkScrollbar(guiframe, orientation='horizontal', command=guicanvs.xview,bg_color='#030e11') #scrollbar direita
guicanvs.grid(row=0,column=0,sticky='nsew')
guivscrol.grid(row=0,column=1,rowspan=2,sticky='nsew')
guihscrol.grid(row=1,column=0,sticky='nsew')

guicanvs.columnconfigure(0, weight=1)
guicanvs.rowconfigure(0, weight=1)
containerframe = ctk.CTkFrame(guicanvs,fg_color='#030e11') # ContainerFrame 
containerframe.grid(row=0,column=0,sticky='nsew')

guicanvs.create_window((0,0), width=ww/2-17, window=containerframe, anchor='nw', tags=('canwin'))

containerframe.bind('<Configure>', lambda e: guicanvs.configure(scrollregion=guicanvs.bbox('all')))
guicanvs.configure(yscrollcommand=guivscrol.set, xscrollcommand=guihscrol.set)

containerframe.columnconfigure([0,1,2], weight=1)

graphframe.grid_propagate(0)
graphframe.columnconfigure(0, weight=1)
graphframe.rowconfigure(0, weight=1)
plotcanvs = ctk.CTkCanvas(graphframe,highlightthickness=0, width=ww/2,bg='#041216')       # cores tela canvas e tamanhop
plotcanvs.grid(row=0,column=0,sticky='nsew')

 # Tamanho e largura da tela do canvas
width = plotcanvs.winfo_width()
height = plotcanvs.winfo_height()

                                                           #Variaveis
letter_coords = {}
Pos_letra = 0                                                        # posição atual do alfabeto 
letter_coords = {}                                                   # Dicionário para armazenar as coordenadas de cada letra

v_posição_x = []                                                     # cria uma lista para armazenar as posições X dos nós
v_posição_x.clear()                                                  # limpa a lista v_posição_x
v_posição_y = []                                                     # cria uma lista para armazenar as posições Y dos nós
v_posição_y.clear()                                                  # limpa a lista v_posição_y
v_p_barras = []                                                      # cria uma lista para armazenar as posições das barras

lista_de_entradas_barras = []                                        # cria uma lista para armazenar as entradas das barras
lista_de_entradanos_x = []                                           # cria uma lista para armazenar os nós
lista_de_entradanos_y = []                                           # cria uma lista para armazenar os nós
contador_de_linhas = int(4)                                          # variavel usada para contar linhas e server de base para onde imprimir os dados na tela 
num_barras = 0
entrada_barras1 = 0
entrada_barras2 = 0
x = 0
y = 0 
E = float('210000')                                                  # elasticidade do aço 


def draw_cartesian_plane():
    plotcanvs.delete("cartesian_plane")  # Remove linhas existentes antes de redesenhar
    width = plotcanvs.winfo_width()
    height = plotcanvs.winfo_height()
    plotcanvs.create_line(0, height / 2, width, height / 2, fill="white", tags="cartesian_plane")
    plotcanvs.create_line(width / 2, 0, width / 2, height, fill="white", tags="cartesian_plane")
    
    # Add labels for the x and y axes
    for i in range(-10, 11):
        if i == 0:
            x = width / 2
            y = height / 2
            plotcanvs.create_text(x, y + 10, text=str(i), fill="white", tags="cartesian_plane")
        else:
            x = width / 2 + i * 35
            y = height / 2
            plotcanvs.create_text(x, y + 10, text=str(i), fill="white", tags="cartesian_plane")
        
    for i in range(-10, 11):
        if i != 0:
            x = width / 2
            y = height / 2 - i * 35
            plotcanvs.create_text(x - 10, y, text=str(i), fill="white", tags="cartesian_plane")

# Chama a função draw_cartesian_plane sempre que o tamanho da tela muda
plotcanvs.bind("<Configure>", lambda event: draw_cartesian_plane())

# Inicializa o plano cartesiano
draw_cartesian_plane()

                                                     #Variaveis



def draw_circle(x, y):
    width = plotcanvs.winfo_width()
    height = plotcanvs.winfo_height()
    x_coord = width / 2 + x * 35
    y_coord = height / 2 - y * 35
    tam = 3
    global Pos_letra
    global letter_coords                                       
    x = int()
    y = int()
    plotcanvs.create_oval(x_coord - tam, y_coord - tam, x_coord + tam, y_coord + tam, fill="#cccfd0", tags="cartesian_plane",outline="white")

    # Obter a letra atual do alfabeto
    current_letter = string.ascii_uppercase[Pos_letra]

    # Criar o texto com a letra atual
    plotcanvs.create_text(x_coord + 10, y_coord, text=current_letter, font=("Arial", 12), tags="cartesian_plane", fill="#cccfd0")

    # Armazenar as coordenadas da letra no dicionário
    letter_coords[current_letter] = (x_coord, y_coord)

    #print(letter_coords)

    # Atualizar a posição atual no alfabeto
    Pos_letra = (Pos_letra + 1) % len(string.ascii_uppercase)
    #print(f"A letra '{current_letter}' foi adicionada ao dicionário com as coordenadas ({x_coord}, {y_coord})") teste para ver se a variavel foi adicionada
    return
def draw_barra(letter1, letter2): # função para desenhar a barra
    global letter_coords                                       
    x1, y1 = letter_coords[letter1]
    x2, y2 = letter_coords[letter2]
    plotcanvs.create_line(x1, y1, x2, y2, fill="#cccfd0", tags="cartesian_plane", width=3)
    return


# caixa de entrada de dados dos nós 
label = ctk.CTkLabel (containerframe , text = "Numero de nós:",text_color='white',)
label.grid (column = 0, row = 0)
entrada_nos = ctk.CTkEntry (containerframe ,width=100,border_color='#030e11')                              # cria uma caixa de entrada do tamanho 10
entrada_nos.grid(column=1, row=0)

# caixa de entrada de dados das barras
label = ctk.CTkLabel(containerframe , text = "Numero de barras:",text_color='white')
label.grid (column = 0, row = 1)
entrada_vigas = ctk.CTkEntry (containerframe,width=100,border_color='#030e11',)                            # cria uma caixa de entrada do tamanho 10
entrada_vigas.grid(column=1, row=1)       
                                                                     # obtem a quantidade de barras do usuario   

botão_confirmar = ctk.CTkButton(containerframe, text="proximo", command=lambda: botão_confirmar()) # usa a função Button para criar um botão 
botão_confirmar.grid(column=0, row=2)



def botão_confirmar():                                               # função botão confirmar pegar os numeros de nós e barras executa um for para criar as caixas de entrada de dados dos nós
    global num_barras
    global lista_de_entradanos_y
    global lista_de_entradanos_x     
    num_barras = int(entrada_vigas.get()) 
    linhas = int (contador_de_linhas)                                # repasando o valor de contador_de_linhas para a variavel linhas para ser usado na função
    entrada_nos_int = int(entrada_nos.get())                         # transformar a variavel entradanos no tipo INT e repasa para a variavel entrada_nos_int para ser usada na função                        


    for i in range(entrada_nos_int):                                 # for para criar as caixas de entrada de dados dos nós
        linhas = linhas + 1                                          # adicinado 1 a variavel linhas para pular uma linha na tela ante de imprimir a mensagem
        label = ctk.CTkLabel (containerframe , text = "posição X e Y do nó " + str(i+1) + ":",text_color='white')      
        label.grid (column = 0, row =linhas)   
        
        caixa = ctk.CTkEntry (containerframe,width=100,border_color='#071e26',)# cria uma caixa de entrada para pegar as cordenada do pontos
        caixa.grid(column=1, row=linhas)
        lista_de_entradanos_x.append(caixa)                          # adicinando o valor que foi inserido na caixa de entrada a uma lista para salvar as cordenadas dos nós
            
                                        
        caixa = ctk.CTkEntry (containerframe ,width=100,border_color='#071e26',)# cria uma caixa de entrada para pegar as cordenada do pontos
        caixa.grid(column=2, row=linhas)                             # marcando onde ele vai ser impressa na tela
        lista_de_entradanos_y.append(caixa)                          # adicinando o valor que foi inserido na caixa de entrada a uma lista para salvar as cordenadas dos nós


        for i in lista_de_entradanos_x:
            if i ==  0:
                lista_de_entradanos_x.remove(i)     

        for i in lista_de_entradanos_y:
            if i ==  0:
                lista_de_entradanos_y.remove(i)                  
    
    botão_confirmar = ctk.CTkButton(containerframe, text="proximo", command=lambda: botão_proximo()) # usa a função Button para criar um botão que ativara a proxima etapa do programa que é pegar as cordenadas das barras 
    botão_confirmar.grid(column=0, row=linhas+1)

    
    return linhas                                                    # retorna o valor de linhas para ser usado na função botão_proximo


def botão_proximo():                                                 # função botão proximo pega os numeros de barras executa um for para criar as caixas de entrada de dados das barras 
    global v_posição_x                                               # pega a lista v_posição_x para ser usada na função
    global v_posição_y      
    global letter_coords
    global lista_de_entradanos_y
    global lista_de_entradanos_x                                               
    global num_barras
    global entrada_barras1
    global entrada_barras2
    print(v_posição_x)
      
    entrada_vigas_int = int(entrada_vigas.get())                     # transformar as duas varias entradavigas e entradanos no tipo INT e repasa para a variavel entrada_vigas_int para ser usada na função 
    linhas = botão_confirmar()                                       # recebe a variavel linhas da função anterior botão_confirmar para continuar a contagem de linhas
    #linhas = [0]                                                    # zera a variavel linhas para ser usada na função
    linhas = linhas + 2                                              # adiciona 2 a variavel linhas para pular duas linhas na tela ante de imprimir a mensagem
    tamanho_lista1 = len(lista_de_entradanos_x)                      # len é uma função que pega o tamanho da lista para ser usado no f
    for i in range(tamanho_lista1):
        if lista_de_entradanos_x[i].get() != '':
            v_posição_x.append(int(lista_de_entradanos_x[i].get()))      # esse funciona para pegar o valor da caixa de entrada
            v_posição_y.append(int(lista_de_entradanos_y[i].get()))      # esse funciona para pegar o valor da caixa de entrada
            x = v_posição_x[i]
            y = v_posição_y[i]
            print (num_barras)
            draw_circle(x,y)  
     
    for i in range(entrada_vigas_int):                               # for para criar as caixas de entrada de dados das barras
        linhas = linhas +1                                           # adicinado 1 a variavel linhas para pular uma linha na tela ante de imprimir a mensagem
        #usado em teste#result_confirm = ctk.CTkLabel(containerframe,text = ("Posicoes salvadas com sucesso" + str(aleatorio)))#usado em teste#
        #usado em teste#result_confirm.grid(column=0, row=linhas+1, columnspan=3)#usado em teste#
    
        '''
        caixa = ctk.CTkEntry (containerframe,width=100,border_color='#071e26')# cria uma caixa de entrada para pegar as cordenada do pontos
        caixa.grid(column=1, row=linhas)                             # marcando onde ele vai ser impressa na tela
        lista_de_entradanos_x.append(caixa)                          # adicinando o valor que foi inserido na caixa de entrada a uma lista para salvar as cordenadas dos nós
        '''    
    for i in range(num_barras):
        label = ctk.CTkLabel (containerframe , text = "diga entre quais nós estão a barra " + str(i+1) + ":",text_color='white')      
        label.grid (column = 0, row = linhas)                        # imprimindo mensagem para as barras
        entrada_barras1= ctk.CTkEntry (containerframe,width=100,border_color='#071e26')                    # cria uma caixa de entrada do tamanho 100
        entrada_barras1.grid(column=1, row=linhas)                    # para receber as cordenadas das barras
        entrada_barras2 = ctk.CTkEntry (containerframe ,width=100,border_color='#071e26')                    # cria uma caixa de entrada do tamanho 100
        entrada_barras2.grid(column=2, row=linhas)                    # para receber a segunda cordenada da barra
        linhas = linhas +1                                            # adicinado 1 a variavel linhas para pular uma linha na tela ante de imprimir a mensagem

   

        
    button_confirmar = ctk.CTkButton(containerframe, text="Confirmar", command=lambda: Desenhar_barra()) # usa a função Button para criar um botão que ativara a proxima etapa do programa que é pegar as cordenadas das barras 
    button_confirmar.grid(column=0, row=linhas+1)

    return
def Desenhar_barra():
    global letter_coords 
    global num_barras
    global entrada_barras1
    global entrada_barras2
    for i in range(num_barras):
    # Obter as letras correspondentes às coordenadas da barra
     letra1 = entrada_barras1.get()
     letra2 = entrada_barras2.get()
    
    # Obter as coordenadas correspondentes às letras do dicionário "letter_coords"
    x1, y1 = letter_coords[letra1]
    x2, y2 = letter_coords[letra2]
    
    # Chamar a função "draw_barra" com as coordenadas obtidas
    draw_barra(letra1, letra2)    
    return




root.mainloop() # Fim da janela
