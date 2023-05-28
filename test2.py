
import tkinter as tk
import math

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        # Criando linhas
        self.canvas.create_line(0, 0, 500, 0, fill='red')
        self.canvas.create_line(0, 0, 0, 500, fill='red')
        self.canvas.create_line(0, 0, 0, 0, fill='red')
        # Definindo largura e altura de linhas
        self.canvas.create_line(0, 0, 500, 0, width=1, fill='red')
        self.canvas.create_line(0, 0, 0, 500, width=1, fill='red')
        self.canvas.create_line(0, 0, 0, 0, width=1, fill='red')

if __name__ == '__main__':
    app = App(tk.Tk())
    app.mainloop()
