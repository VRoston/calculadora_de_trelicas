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
b_inicial =[]
b_final = []
mat = numpy.array ([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]])



entrada_vigas = '2'
A = float('200')
E = float('210000')
b = 0
l = 0
a1 = 0
b1 = 0
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
        global a1
        global b1
        global xco
        global yco
        tamanho_lista1 = len(lista_entradax)       
        num_barra =int(entrada_vigas.get())
       # print('numeros de barras')
       # print(num_barra)

        for i in range(tamanho_lista1):
            if lista_entradax[i].get() != '':
                xco.append(float(lista_entradax[i].get()))      # esse funciona para pegar o valor da caixa de entrada das coordenadas
                yco.append(float(lista_entraday[i].get()))      # esse funciona para pegar o valor da caixa de entrada das coordenadas
                
        
        for i in range(num_barra):
            label = ctk.CTkLabel (containerframe , text = "Entre com o nó inicial e final " + str(i+1) + ":",text_color='white')      
            label.grid (column = 0, row =linhas)
            a1 = ctk.CTkEntry (containerframe,width=100,border_color='#030e11',)                            # cria uma caixa de entrada do tamanho 10
            a1.grid(column=1, row=linhas)        
            inicial_barra.append(a1)

            b1 = ctk.CTkEntry (containerframe,width=100,border_color='#030e11',)                            # cria uma caixa de entrada do tamanho 10
            b1.grid(column=2, row=linhas)   
            final_barra.append(b1)
            linhas = linhas + 2   
    
    
        botão_confirmar = ctk.CTkButton(containerframe, text="Ok", command=lambda: confirmar3()) # usa a função Button para criar um botão 
        botão_confirmar.grid(column=0, row=linhas+1)


    
    def confirmar3():
        global x1 , mat
        global y1
        global x2
        global y2
        global xcon
        global ycon
        global a 
        global b
        global A
        global E
        global lq
        global linhas
        global cos
        global sin
        global snofel
        global enofel
        global lenofel
        global elcon
        global cosofel
        global sinofel
        global te
        global tn
        global b_inicial
        global b_final
        global inicial_barra
        global final_barra
        global elstmat
        elstmat = [] 
        gstmatmap = []  
        displist = []
        forcelist = []
        for i in range(te):
          
            b_inicial.append(int(inicial_barra[i].get()))      # esse funciona para pegar o valor da caixa de entrada das coordenadas
            b_final.append(int(final_barra[i].get()))      # esse funciona para pegar o valor da caixa de entrada das coordenadas
                
            ##print(yco)

        for i in range(te):  
            a = b_inicial[i]
            b = b_final[i]
           ##print(b)
            x1 = float(xco[a-1])
            y1 = float(yco[a-1])
            x2 = float(xco[b-1])
            y2 = float(yco[b-1])
            l = math.sqrt((x2-x1)**2+(y2-y1)**2)
            con = A*E/l
            cos = (x2-x1)/l
            sin = (y2-y1)/l
    
            snofel.append(a)
            enofel.append(b)
            lenofel.append(l)
            elcon.append(con)
            cosofel.append(cos)
            sinofel.append(sin)
            cc = float(cosofel[i])**2
            ss = float(sinofel[i])**2
            cs = float(cosofel[i])*float(sinofel[i])
            
            mat = elcon[i]*numpy.array([[cc, cs, -cc, -cs],
                      [cs, ss, -cs, -ss],
                      [-cc, -cs, cc, cs],
                      [-cs, -ss, cs, ss]])
            elstmat.append(mat)
            #print (elstmat)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            m = snofel[i]*2                     ## taking the start node of element(i) and multiply by 2
            n = enofel[i]*2                     ## taking the end node of element(i) and multiply by 2
            add = [m-1, m, n-1, n]              ## Address of columns and rows of gstmatmap for elemet(i)
                                            # if startnode is 1 and end node is 2 then add=[1,2,3,4]
                                            # if startnode is 1 and end node is 3 then add=[1,2,5,6]
            gmat = numpy.zeros((tn*2, tn*2))    ## global stiffness matrix loaded with zeros for element(i)
            elmat = elstmat[i]                  ## taking the element stiffness matrix of element(i)
            for j in range(4):                  
                for k in range(4):              
                    a = add[j]-1                ## addressing row of GST matrix for element(i)
                    b = add[k]-1                ## addressing column of GST matrix for element(i)
                    gmat[a,b] = elmat[j,k]      ## updating the values in GST matrix with EST matrix of element(i)
            gstmatmap.append(gmat)              ## storing the resultant matrix in gstmatmap list

        GSM = numpy.zeros((tn*2, tn*2))         ## creating an empyty GSM matrix
        for mat in gstmatmap:
            GSM = GSM+mat                       ## adding all the matrix in the gstmatmap list
                                            # this will result in assembled stiffness matrix of the truss structure

        #print('\nGlobal Stiffness Matrix of the Truss\n')
        #print(numpy.around(GSM, 3))
 
        for i in range(tn):
            a = str('u')+str(i+1)
            displist.append(a)
            b = str('v')+str(i+1)
            displist.append(b)
            c = str('fx')+str(i+1)
            forcelist.append(c)
            d = str('fy')+str(i+1)
            forcelist.append(d)

        print(displist)
        print(forcelist)













           
       
        
          
  
  
    

   


        
    



main()
root.mainloop()
