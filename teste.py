import tkinter as tk
import string

# Inicializar a posição atual no alfabeto
Pos_letra = 0

# Dicionário para armazenar as coordenadas de cada letra
letter_coords = {}

# Criar a janela principal
root = tk.Tk()
root.title("Desenhar círculos e linhas")

# Criar o canvas
plotcanvs = tk.Canvas(root, width=600, height=400, bg="#1e1e1e")
plotcanvs.pack()

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

    # Armazenar as coordenadas da letra no dicionário
    letter_coords[current_letter] = (x_coord, y_coord)

    # Atualizar a posição atual no alfabeto
    Pos_letra = (Pos_letra + 1) % len(string.ascii_uppercase)

def draw_line_between_letters(letter1, letter2):
    x1, y1 = letter_coords[letter1]
    x2, y2 = letter_coords[letter2]
    plotcanvs.create_line(x1, y1, x2, y2, fill="#cccfd0", tags="cartesian_plane", width=2)



# Desenhar dois círculos com as letras 'A' e 'B'
draw_circle(1, 1)  # Círculo 'A'
draw_circle(2, 2)  # Círculo 'B'

# Desenhar uma linha entre os círculos 'A' e 'B'
draw_line_between_letters('A', 'B')

# Iniciar o loop principal
root.mainloop()
