from tkinter import *
import time

button = []
DispTXT = ["Play as Red!", "Play as Blue!",
           "Let the Computer play!", "Two players!"]

root = Tk()
for i in range(4):
    b = Button(root, text=DispTXT[i], command=lambda i=i: print(DispTXT[i]))
    b.pack()
    button.append(b)

root.mainloop()
