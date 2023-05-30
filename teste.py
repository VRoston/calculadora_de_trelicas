import tkinter as tk
import string
9k-0

# Inicializar a posição atual no alfabeto
Pos_letra = 0


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
def draw_circle(x, y):
    width = plotcanvs.winfo_width()
    height = plotcanvs.winfo_height()
    x_coord = width / 2 + x * 35
    y_coord = height / 2 - y * 35
    tam = 3
    global Pos_letra
    x = int()
    y = int()
    plotcanvs.create_oval(x_coord - tam, y_coord - tam, x_coord + tam, y_coord + tam, fill="#cccfd0", tags="cartesian_plane",outline="white")

    # Obter a letra atual do alfabeto
    current_letter = string.ascii_uppercase[Pos_letra]

    # Criar o texto com a letra atual
    plotcanvs.create_text(x_coord + 10, y_coord, text=current_letter, font=("Arial", 12), tags="cartesian_plane", fill="#cccfd0")

    # Atualizar a posição atual no alfabeto
    Pos_letra = (Pos_letra + 1) % len(string.ascii_uppercase)

    return x_coord, y_coord

def draw_line_between_circles(x1, y1, x2, y2):
    plotcanvs.create_line(x1, y1, x2, y2, fill="#cccfd0", tags="cartesian_plane", width=2)



# Exemplo de uso das funções
x1, y1 = draw_circle(1, 1)
x2, y2 = draw_circle(2, 2)
draw_line_between_circles(x1, y1, x2, y2)

# Iniciar o loop principal
root.mainloop()

