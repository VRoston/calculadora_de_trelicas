import math
import numpy
import tkinter as tk
import customtkinter  as ctk 

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


####____________________________________________________________________________________####

labellist=[]
entrylist=[]
buttonlist=[]

inputlist=[]

xco=[]
yco=[]

xplotpts=[]
yplotpts=[]

snofel=[]
enofel=[]

lenofel=[]
elcon=[]
cosofel=[]
sinofel=[]

elstmat=[]
gstmatmap=[]

displist=[]
forcelist=[]
lista_entradax=[]
lista_entraday=[]
inicial_barra=[]
final_barra=[] 
entrada_vigas = '2'
A = float('200')
E = float('210000')

numpymatlist=[]
linhas = 1
te = 0
tn = 0
####____________________________________________________________________________________####




def main():
   
    global entrada_vigas
    # caixa de entrada de dados dos nós 
    label = ctk.CTkLabel (containerframe , text = "Numero de nós:",text_color='white',)
    label.grid (column = 0, row = 0)
    entrada_no = ctk.CTkEntry (containerframe ,width=100,border_color='#030e11')                              # cria uma caixa de entrada do tamanho 10
    entrada_no.grid(column=1, row=0)
    # caixa de entrada de dados das barras
    label = ctk.CTkLabel(containerframe , text = "Numero de barras:",text_color='white')
    label.grid (column = 0, row = 1)
    entrada_vigas= ctk.CTkEntry (containerframe,width=100,border_color='#030e11',)                            # cria uma caixa de entrada do tamanho 10
    entrada_vigas.grid(column=1, row=1)       
                                                                     # obtem a quantidade de barras do usuario   

    botão_confirmar = ctk.CTkButton(containerframe, text="proximo", command=lambda: confirmar()) # usa a função Button para criar um botão 
    botão_confirmar.grid(column=0, row=2)
    def confirmar():
        global xco 
        global yco 
        global linhas
        global te
        global tn
        global lista_entraday
        global lista_entradax
        global supA
        linhas = linhas + 2
        tn = int(entrada_no.get()) 
        te = int(entrada_vigas.get()) 


        #print(tn)
        #print(te)

    
        for i in range(tn):
            label = ctk.CTkLabel (containerframe , text = "posição X e Y do nó " + str(i+1) + ":",text_color='white')      
            label.grid (column = 0, row =linhas)   
               
            x = ctk.CTkEntry (containerframe,width=100,border_color='#071e26',)# cria uma caixa de entrada para pegar as coordenada do pontos
            x.grid(column=1, row=linhas)
            lista_entradax.append(x)
                                 
            y= ctk.CTkEntry (containerframe ,width=100,border_color='#071e26',)# cria uma caixa de entrada para pegar as coordenada do pontos
            y.grid(column=2, row=linhas)                             # marcando onde ele vai ser impressa na tela
            lista_entraday.append(y)
            linhas = linhas +2


        botão_confirmar = ctk.CTkButton(containerframe, text="proximo", command=lambda: confirmar2()) # usa a função Button para criar um botão 
        botão_confirmar.grid(column=0, row=linhas+1)



    def confirmar2(): 
        global linhas
        global lista_entradax
        global lista_entraday  
        linhas = linhas + 2
        global inicial_barra 
        global entrada_vigas
        global final_barra                                              # adiciona 2 a variavel linhas para pular duas linhas na tela ante de imprimir a mensagem
        tamanho_lista1 = len(lista_entradax)       
        A = 200
        num_barra =int(entrada_vigas.get())
        print(num_barra)

        for i in range(tamanho_lista1):
            if lista_entradax[i].get() != '':
                xco.append(float(lista_entradax[i].get()))      # esse funciona para pegar o valor da caixa de entrada das coordenadas
                yco.append(float(lista_entraday[i].get()))      # esse funciona para pegar o valor da caixa de entrada das coordenadas
        
        for i in range(num_barra):
            label = ctk.CTkLabel (containerframe , text = "Entre com o nó inicial e final " + str(i+1) + ":",text_color='white')      
            label.grid (column = 0, row =linhas)
            a = ctk.CTkEntry (containerframe,width=100,border_color='#030e11',)                            # cria uma caixa de entrada do tamanho 10
            a.grid(column=1, row=linhas)        
            inicial_barra.append(a)
            b = ctk.CTkEntry (containerframe,width=100,border_color='#030e11',)                            # cria uma caixa de entrada do tamanho 10
            b.grid(column=2, row=linhas)   
            linhas = linhas + 2   
    
    
    
    
    
    return


main()
root.mainloop()
