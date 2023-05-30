import tkinter as tk
from tkinter import messagebox

'''

    F1 é a força na primeira extremidade da barra.
    F2 é a força na segunda extremidade da barra.
    F3 é a força na terceira extremidade da barra.
    Fx é a força horizontal aplicada na barra.
    Fy é a força vertical aplicada barra.
    L é o comprimento da barra.

'''

def calcular_forcas(nodo):
    try:
        Fx = float(entry_Fx.get())
        Fy = float(entry_Fy.get())
        L = float(entry_L.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    if nodo == "A":
        F1 = Fy
        F2 = Fx
        F3 = -((F1 * L) / L)
    elif nodo == "B":
        F1 = F
        F2 = -((F1 * L) / L)
        F3 = Fy
    elif nodo == "C":
        F1 = -((Fy * L) / L)
        F2 = Fx
        F3 = Fy

    resultado.set(f"F1 = {F1:.2f} N, F2 = {F2:.2f} N, F3 = {F3:.2f} N")

def desenhar_trelica():
    canvas.delete("all")
    canvas.create_line(50, 150, 150, 50,width='1.5')
    canvas.create_line(150, 50, 250, 150,width='1.5')
    canvas.create_line(50, 150, 250, 150,width='1.5')
    canvas.create_text(50, 150, text="A  ")
    canvas.create_text(150, 50, text="  B")
    canvas.create_text(250, 150, text="  C")

root = tk.Tk()
root.title("Método dos Nós para Treliças")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

canvas = tk.Canvas(frame, width=300, height=200)
canvas.pack()

desenhar_trelica()

label_Fx = tk.Label(frame, text="Força horizontal (Fx):")
label_Fx.pack()
entry_Fx = tk.Entry(frame)
entry_Fx.pack()

label_Fy = tk.Label(frame, text="Força vertical (Fy):")
label_Fy.pack()
entry_Fy = tk.Entry(frame)
entry_Fy.pack()

label_L = tk.Label(frame, text="Comprimento da barra 1 (L):")
label_L.pack()
entry_L = tk.Entry(frame)
entry_L.pack()



button_desenhar = tk.Button(frame, text="Desenhar Treliça", command=desenhar_trelica)
button_desenhar.pack()

button_calcular_A = tk.Button(frame, text="Calcular Forças em A", command=lambda: calcular_forcas("A"))
button_calcular_A.pack()

button_calcular_B = tk.Button(frame, text="Calcular Forças em B", command=lambda: calcular_forcas("B"))
button_calcular_B.pack()

button_calcular_C = tk.Button(frame, text="Calcular Forças em C", command=lambda: calcular_forcas("C"))
button_calcular_C.pack()

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado)
label_resultado.pack()

root.mainloop()
