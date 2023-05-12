import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300, bg='white')
canvas.pack()

x0, y0 = 0, 0
x1, y1 = 0, 0

def on_first_right_click(event):
    global x0, y0, x1, y1
    x0, y0 = event.x, event.y
    canvas.create_line(0, 0, x0, y0, fill="red")

def on_second_right_click(event):
    global x1, y1
    x1, y1 = event.x, event.y
    canvas.create_line(x1, y1, 0, 0, fill="black")

canvas.bind('<Button-1>', on_first_right_click)
canvas.bind('<Button-3>', on_second_right_click)

root.mainloop()
