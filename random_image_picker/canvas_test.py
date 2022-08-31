import tkinter as tk
from random import randint
import tkinter.font as font
import time
from turtle import back
from PIL import Image, ImageTk


window = tk.Tk()

canvas = tk.Canvas(window)
canvas.pack()

img = ImageTk.PhotoImage(file='imgs/2.png')
canvas.create_image(10, 10, image=img)

window.mainloop()
