import tkinter as tk
from tkinter import *

win = tk.Tk()
inner_button = [['button_0_0', 'button_1_0', 'button_2_0', 'button_3_0', 'button_4_0', 'button_5_0', ],
                ['button_0_2', 'button_1_2', 'button_2_2',
                    'button_3_2', 'button_4_2', 'button_5_2', ],
                ['button_0_3', 'button_1_3', 'button_2_3',
                    'button_3_3', 'button_4_3', 'button_5_3', ],
                ['button_0_4', 'button_1_4', 'button_2_4',
                    'button_3_4', 'button_4_4', 'button_5_4', ],
                ['button_0_1', 'button_1_1', 'button_2_1',
                    'button_3_1', 'button_4_1', 'button_5_1', ],
                ['button_0_5', 'button_1_5', 'button_2_5', 'button_3_5', 'button_4_5', 'button_5_5', ], ]
for i in range(6):
    for j in range(6):
        frame = tk.Frame(
            master=win,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        print(i, j)
        print(inner_button[i][j])
        inner_button[i][j] = Button(
            frame, text='{}'.format(inner_button[i][j]))

        inner_button[i][j].pack()

        # label = tk.Label(master=frame, text="Row {}\nColumn {}".format(i, j))
        # label.pack()

win.mainloop()
