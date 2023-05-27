import tkinter as tk                                                 # importa a biblioteca tkinter para usar com a API tk
import numpy as np           
import math                                        
import customtkinter  as ctk                                         # biblioteca

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
containerframe = tk.Frame(guicanvs,)
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


v_posição_x = []
v_posição_y = []
 




root.mainloop()