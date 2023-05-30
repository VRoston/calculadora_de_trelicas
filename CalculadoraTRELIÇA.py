import tkinter as tk
from tkinter import messagebox

def calcular_forcas():
    try:
        Fx = float(entry_Fx.get())
        Fy = float(entry_Fy.get())
        L = float(entry_L.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    F1 = Fy
    F2 = Fx
    F3 = -((F1 * L) / L)

    resultado.set(f"F1 = {F1:.2f} N, F2 = {F2:.2f} N, F3 = {F3:.2f} N")

root = tk.Tk()
root.title("Método dos Nós para Treliças")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label_Fx = tk.Label(frame, text="Força horizontal (Fx):")
label_Fx.grid(row=0, column=0, sticky="e")
entry_Fx = tk.Entry(frame)
entry_Fx.grid(row=0, column=1)

label_Fy = tk.Label(frame, text="Força vertical (Fy):")
label_Fy.grid(row=1, column=0, sticky="e")
entry_Fy = tk.Entry(frame)
entry_Fy.grid(row=1, column=1)

label_L = tk.Label(frame, text="Comprimento da barra (L):")
label_L.grid(row=2, column=0, sticky="e")
entry_L = tk.Entry(frame)
entry_L.grid(row=2, column=1)

button_calcular = tk.Button(frame, text="Calcular Forças", command=calcular_forcas)
button_calcular.grid(row=3, columnspan=2, pady=10)

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado)
label_resultado.grid(row=4, columnspan=2)

root.mainloop()
