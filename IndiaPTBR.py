import tkinter as tk                                                 # importa a biblioteca tkinter para usar com a API tk
import numpy as np           
import math                                        
import customtkinter  as ctk                                         # biblioteca

# Variaveis
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

numpymatlist=[]

np.set_printoptions(3, suppress=True)

root= ctk.CTk()  # criar a nossa janela

#                           Tamanho Da tela
root.title('Calculadora de treliçãs')
root._set_appearance_mode("dark")
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = int(5*sw/6)
wh = int(5*sh/6)
who = int(1*(sh-wh)/3)
wwo = int((sw-ww)/2)
root.minsize(800,600)                                                   # Tamanho minimo da janela 
winsize = str(ww)+'x'+str(wh)+'+'+str(wwo)+'+'+str(who)                       
root.geometry(winsize)                                                  # Tamanho da janela ao abrir

# Criação dos Frames
root.columnconfigure([0,1], weight=1)
root.rowconfigure(1, weight=1)
titleframe = ctk.CTkFrame(root)                    # Frame da tela do Título "analisador de treliçãs 2d"
guiframe = ctk.CTkFrame(root)                      # Frama aonde o usuario digita
graphframe = ctk.CTkFrame(root)                    # frame do desenho
titleframe.grid(row=0,column=0,columnspan=2,sticky='nsew')
guiframe.grid(row=1,column=0,sticky='nsew')
graphframe.grid(row=1,column=1,sticky='nsew')

# configurando o frame do title
titleframe.columnconfigure(0, weight=1)
titlelbl = tk.Label(titleframe, text='Analisador de treliças 2d', font=('Arial 25 bold'))
titlelbl.grid(row=0,column=0,sticky='nsew')

# Configurando o frame do gui
guiframe.columnconfigure(0, weight=1)
guiframe.rowconfigure(0, weight=1)
guiframe.grid_propagate(0)

guicanvs = tk.Canvas(guiframe, bg='blue', highlightthickness=0)
guivscrol = tk.Scrollbar(guiframe, orient='vertical', command=guicanvs.yview)
guihscrol = tk.Scrollbar(guiframe, orient='horizontal', command=guicanvs.xview)
guicanvs.grid(row=0,column=0,sticky='nsew')
guivscrol.grid(row=0,column=1,rowspan=2,sticky='nsew')
guihscrol.grid(row=1,column=0,sticky='nsew')

guicanvs.columnconfigure(0, weight=1)
guicanvs.rowconfigure(0, weight=1)
containerframe = tk.Frame(guicanvs, bg='red')
containerframe.grid(row=0,column=0,sticky='nsew')

guicanvs.create_window((0,0), width=ww/2-17, window=containerframe, anchor='nw', tags=('canwin'))

containerframe.bind('<Configure>', lambda e: guicanvs.configure(scrollregion=guicanvs.bbox('all')))
guicanvs.configure(yscrollcommand=guivscrol.set, xscrollcommand=guihscrol.set)

containerframe.columnconfigure([0,1,2], weight=1)

graphframe.grid_propagate(0)
graphframe.columnconfigure(0, weight=1)
graphframe.rowconfigure(0, weight=1)
plotcanvs = tk.Canvas(graphframe, bg='gray',highlightthickness=0, width=ww/2)
plotcanvs.grid(row=0,column=0,sticky='nsew')

def btnprs(btn):

    ###_____________________________________________________________________###

    if btn == 'btn1':
        def drawcoinp():
            tn = int(entrylist[0].get())
            te = int(entrylist[1].get())
            inputlist.append(tn)
            inputlist.append(te)
            for i in range(tn):                
                t = 'Digita A Coordenada do X e Y do nó '+str(i+1)+' em MM : '
                lbl = tk.Label(containerframe, text=t)
                labellist.append(lbl)
                lbl.grid(row=2+i,column=0,sticky='nsew')
                xent = tk.Entry(containerframe)
                entrylist.append(xent)
                yent = tk.Entry(containerframe)
                entrylist.append(yent)
                xent.grid(row=2+i,column=1,sticky='nsew')
                yent.grid(row=2+i,column=2,sticky='nsew')
            btn2 = tk.Button(containerframe, text='Plot', command = lambda: btnprs('btn2'))
            buttonlist.append(btn2)
            btn2.grid(row=2+tn,column=0,columnspan=2,sticky='nsew')
        if len(inputlist)==0:
            drawcoinp()
        else:
            for i in range(2,len(labellist)):
                labellist[i].destroy()
            for i in range(2, len(entrylist)):
                entrylist[i].destroy()
            for i in range(1, len(buttonlist)):
                buttonlist[i].destroy()
                
            del inputlist[0:]
            del labellist[2:]
            del entrylist[2:]
            del buttonlist[1:]
            xco.clear()
            yco.clear()
            xplotpts.clear()
            yplotpts.clear()
            snofel.clear()
            enofel.clear()
            plotcanvs.delete('all')
            drawcoinp()
    ###_____________________________________________________________________###
            
    if btn == 'btn2':
        def getcoordinates():
            btn3 = tk.Button(containerframe, text='OK', command=lambda: btnprs('btn3'))
            buttonlist.append(btn3)
            btn3.grid(row=2+inputlist[0],column=2,columnspan=2,sticky='nsew')
            count=0
            for i in range(inputlist[0]):
                xco.append(float(entrylist[2+count].get()))
                yco.append(float(entrylist[3+count].get()))
                count = count+2
            ###________________###
            def draw():
                plotcanvs.update()
                w = plotcanvs.winfo_width()-30
                h = plotcanvs.winfo_height()-30
                xmax, ymax, xmin, ymin = max(xco), max(yco), min(xco), min(yco)
                if xmin<=0:
                    alpax = w/xmax-xmin
                else:
                    alpax = w/xmax
                if ymin<=0:
                    alpay = h/ymax-ymin
                else:
                    alpay = h/ymax
                for i in range(len(xco)):
                    x, y = int(xco[i]), int(yco[i])
                    vert = (h-alpay*0.8*y)-h/9
                    yplotpts.append(vert)
                    hori = (alpax*0.8*x)+w/8
                    xplotpts.append(hori)
                    x1, y1, x2, y2 = hori-6, vert-6, hori+6, vert+6
                    plotcanvs.create_oval(x1,y1,x2,y2, width=2, fill='blue', tags='nodes')
                    t = 'N'+str(i+1)
                    plotcanvs.create_text(x2+10, y2+10, text=t, font=('Areal 10 bold'), tags='nodenum')
            draw()
            ###______________###
        if len(xco)==0:
            getcoordinates()
        else:
            xco.clear()
            yco.clear()
            xplotpts.clear()
            yplotpts.clear()
            plotcanvs.delete('all')
            for i in range(2, len(buttonlist)):
                buttonlist[i].destroy()
            del buttonlist[2:]
            getcoordinates()



    
root.mainloop()