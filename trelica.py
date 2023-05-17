import tkinter as tk        # importa a biblioteca tkinter para usar com a API tk

root = tk.Tk()             # cria uma janela

canvas = tk.Canvas(root, bg="white", width=1200, height=800)   # cria uma instância de Canvas com o tamanho de 600x400 e com fundo branco
canvas.pack()              # pack a janela, adicionando o canvas

coords = {"x":0,"y":0,"x2":0,"y2":0}    # define uma lista para armazenar as coordenadas das linhas
# mantém uma referência a todas as linhas mantendo-as em uma lista
lines = []
def click(e):
    # define o ponto inicial da linha
    coords["x"] = e.x
    coords["y"] = e.y

    # cria uma linha nesse ponto e a armazena na lista
    lines.append(canvas.create_line(coords["x"],coords["y"],coords["x"],coords["y"], width="5")) #cria a linha

def drag(e):
    # atualize as coordenadas a partir do evento
    coords["x2"] = e.x
    coords["y2"] = e.y

    # mude as coordenadas da ultima linha criada para as coordenadas novas
    canvas.coords(lines[-1], coords["x"], coords["y"], coords["x2"], coords["y2"])

canvas.bind("<ButtonPress-1>", click)            
canvas.bind("<B1-Motion>", drag)                  

root.mainloop()                                # deixa o programa aberto
