import tkinter as tk
from random import randint
import tkinter.font as font
import time
from turtle import back
from PIL import Image, ImageTk
import os
from functools import partial
import threading
import cv2
from os import startfile


# import cv2

# capture = cv2.VideoCapture('imgs/36.mp4')

# while capture.isOpened():
#     run, frame = capture.read()
#     if not run:
#         print("[프레임 수신 불가] - 종료합니다")
#         break
#     img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
#     cv2.imshow('video', frame)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break

# capture.release()
# cv2.destroyAllWindows()


# cap = cv2.VideoCapture("imgs/36.mp4")
# while True:
#     ret, frame = cap.read()

#     cv2.imshow("frame", "frame")
#     key = cv2.waitKey(10)
#     if key == "ord"("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()


picked_numbers = []
img_lists = os.listdir("imgs")
ext_lists = ["jpg", "jpeg", "png", "webp"]
img_name2 = ""
clicked_count = 0
# for i in img_lists:
#     name, ext = i.split('.')
#     ext_lists.append(ext)


def reset_number(event=None):
    label_2_3.configure(bg="black", fg="white")
    label_2_4.configure(bg="black", fg="white")


window = tk.Tk()

myFont = font.Font(size=60, family="Helvetica")
myFont2 = font.Font(size=40, family="Helvetica")

clicked_num = 0
clicked_num2 = 0
base_frame = tk.Frame(window, width=1920, height=1080)
base_frame.pack()
window.attributes("-fullscreen", True)


def end_fullscreen2(event=None):
    window.attributes("-fullscreen", False)


def re_fullscreen(event=None):
    window.attributes("-fullscreen", True)


window.bind("q", end_fullscreen2)
window.bind("<F11>", re_fullscreen)


frame_top = tk.Frame(base_frame)
frame_top.pack()

frame_bottom = tk.Frame(base_frame, height=100)
frame_bottom.pack()

# picked_numbers = ['11','12','13','14','15','16','17','18']
def button_click(event=None):
    global clicked_num
    global clicked_num
    global clicked_num2
    global picked_numbers
    global img_name
    global img_name2
    global img_canvas
    global clicked_num_final
    label_2_3.configure(bg="white", fg="black")
    clicked_num = label_2_3["text"]
    label_2_4.configure(bg="white", fg="black")
    clicked_num2 = label_2_4["text"]

    if clicked_num == "0":
        clicked_num = ""
    clicked_num_final = clicked_num + clicked_num2
    if clicked_num_final in picked_numbers:
        label_2_3.configure(bg="black", fg="white")
        label_2_4.configure(bg="black", fg="white")


def button_click2(event=None):
    if int(clicked_num_final) < 44:
        if clicked_num_final not in picked_numbers:
            print(clicked_num_final)

            # # Load the .gif image file.
            # img = ImageTk.PhotoImage(Image.open('imgs/1.png'))
            if clicked_num_final in ["36", "41"]:
                clicked_num_video = clicked_num_final + ".mp4"
                vid_path = f"C:/Users/Jay/Desktop/random_image_picker/imgs/{clicked_num_video}"

                startfile(vid_path)

                # capture = cv2.VideoCapture(vid_path)

                # while capture.isOpened():
                #     run, frame = capture.read()
                #     if not run:
                #         print("[프레임 수신 불가] - 종료합니다")
                #         break
                #     img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
                #     img = cv2.resize(
                #         frame, (1900, 1000), interpolation=cv2.INTER_LINEAR
                #     )
                #     cv2.imshow("video", img)
                #     cv2.setWindowProperty(
                #         "video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
                #     )

                #     if cv2.waitKey(30) & 0xFF == ord("q"):
                #         break

                # capture.release()
                # cv2.destroyAllWindows()
                # pass
            else:
                newWindow = tk.Toplevel(window)

                # sets the title of the
                # Toplevel widget
                newWindow.title("Image/Video")

                def end_fullscreen(event=None):
                    newWindow.destroy()

                # sets the geometry of toplevel
                newWindow.attributes("-fullscreen", True)
                newWindow.bind("<Escape>", end_fullscreen)

                img_canvas = tk.Canvas(newWindow, background="gray")
                img_canvas.pack(
                    side="top", padx=0, pady=0, expand=True, fill="both"
                )
                for i in ext_lists:
                    if clicked_num_final in ["5", "6", "14", "28", "32"]:
                        clicked_num_final1 = clicked_num_final + "-1"
                        clicked_num_final2 = clicked_num_final + "-2"
                        if os.path.isfile(f"imgs/{clicked_num_final1}.{i}"):
                            img_name = f"{clicked_num_final1}.{i}"
                            img_name2 = f"{clicked_num_final2}.{i}"

                            time.sleep(0.4)
                            img = Image.open(f"imgs/{img_name}")
                            # resized_image = img.resize((1800, 800), Image.ANTIALIAS)
                            new_img = ImageTk.PhotoImage(img)
                            img_canvas.img = new_img
                            img_canvas.create_image(
                                0, 0, anchor="nw", image=new_img
                            )
                            img_canvas.pack(
                                side="top",
                                padx=0,
                                pady=0,
                                expand=True,
                                fill="both",
                            )

                            # action_with_arg = partial(load_next_img, img_name2)
                            ## second page button
                            def load_next_img(event=None):
                                img = Image.open(f"imgs/{img_name2}")
                                # resized_image = img.resize(
                                #     (1700, 700), Image.ANTIALIAS
                                # )
                                new_img = ImageTk.PhotoImage(img)
                                img_canvas.img = new_img
                                img_canvas.create_image(
                                    0, 0, anchor="nw", image=new_img
                                )

                            second_frame_bottom_button = tk.Button(
                                newWindow,
                                height=2,
                                text="Next",
                                command=load_next_img,
                                borderwidth=0,
                            )

                            second_frame_bottom_button["font"] = myFont2
                            second_frame_bottom_button.pack(side="bottom")

                    elif os.path.isfile(f"imgs/{clicked_num_final}.{i}"):
                        img_name = f"{clicked_num_final}.{i}"

                        time.sleep(0.4)
                        img = Image.open(f"imgs/{img_name}")
                        # resized_image = img.resize((1800, 900), Image.ANTIALIAS)
                        new_img = ImageTk.PhotoImage(img)
                        img_canvas.img = new_img
                        img_canvas.create_image(
                            0, 0, anchor="nw", image=new_img
                        )
            picked_numbers.append(clicked_num_final)
            print(picked_numbers)


frame_bottom_button1 = tk.Button(
    frame_bottom, height=2, text="Pick", command=button_click, borderwidth=0
)
frame_bottom_button1["font"] = myFont2
frame_bottom_button1.pack(side="left")

frame_bottom_button2 = tk.Button(
    frame_bottom, height=2, text="Show", command=button_click2, borderwidth=0
)
frame_bottom_button2["font"] = myFont2
frame_bottom_button2.pack(side="left")

frame_bottom_button = tk.Button(
    frame_bottom, height=2, text="Reset", command=reset_number, borderwidth=0
)
frame_bottom_button["font"] = myFont2
frame_bottom_button.pack(side="right")


label_0_0 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_0["font"] = myFont
label_0_0.grid(row=0, column=0)

label_0_1 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_1["font"] = myFont
label_0_1.grid(row=0, column=1)

label_0_2 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_2["font"] = myFont
label_0_2.grid(row=0, column=2)

label_0_3 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_3["font"] = myFont
label_0_3.grid(row=0, column=3)

label_0_4 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_4["font"] = myFont
label_0_4.grid(row=0, column=4)

label_0_5 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_5["font"] = myFont
label_0_5.grid(row=0, column=5)

label_0_6 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_6["font"] = myFont
label_0_6.grid(row=0, column=6)

label_0_7 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_0_7["font"] = myFont
label_0_7.grid(row=0, column=7)

#####################################################################

label_1_0 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_0["font"] = myFont
label_1_0.grid(row=1, column=0)

label_1_1 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_1["font"] = myFont
label_1_1.grid(row=1, column=1)

label_1_2 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_2["font"] = myFont
label_1_2.grid(row=1, column=2)

label_1_3 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_3["font"] = myFont
label_1_3.grid(row=1, column=3)

label_1_4 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_4["font"] = myFont
label_1_4.grid(row=1, column=4)

label_1_5 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_5["font"] = myFont
label_1_5.grid(row=1, column=5)

label_1_6 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_6["font"] = myFont
label_1_6.grid(row=1, column=6)

label_1_7 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_1_7["font"] = myFont
label_1_7.grid(row=1, column=7)

#####################################################################

label_2_0 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_0["font"] = myFont
label_2_0.grid(row=2, column=0)

label_2_1 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_1["font"] = myFont
label_2_1.grid(row=2, column=1)

label_2_2 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_2["font"] = myFont
label_2_2.grid(row=2, column=2)

label_2_3 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 4)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_3["font"] = myFont
label_2_3.grid(row=2, column=3)

label_2_4 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 9)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_4["font"] = myFont
label_2_4.grid(row=2, column=4)

label_2_5 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_5["font"] = myFont
label_2_5.grid(row=2, column=5)

label_2_6 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_6["font"] = myFont
label_2_6.grid(row=2, column=6)

label_2_7 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_2_7["font"] = myFont
label_2_7.grid(row=2, column=7)
######################################################################

label_3_0 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_0["font"] = myFont
label_3_0.grid(row=3, column=0)

label_3_1 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_1["font"] = myFont
label_3_1.grid(row=3, column=1)

label_3_2 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_2["font"] = myFont
# label_3_2.focus_force()  # 초기 초점 지정
label_3_2.grid(row=3, column=2)

label_3_3 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_3["font"] = myFont
label_3_3.grid(row=3, column=3)

label_3_4 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_4["font"] = myFont
label_3_4.grid(row=3, column=4)

label_3_5 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_5["font"] = myFont
label_3_5.grid(row=3, column=5)

label_3_6 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_6["font"] = myFont
label_3_6.grid(row=3, column=6)

label_3_7 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_3_7["font"] = myFont
label_3_7.grid(row=3, column=7)

##################################################################

label_4_0 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_0["font"] = myFont
label_4_0.grid(row=4, column=0)

label_4_1 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_1["font"] = myFont
label_4_1.grid(row=4, column=1)

label_4_2 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_2["font"] = myFont
label_4_2.grid(row=4, column=2)

label_4_3 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_3["font"] = myFont
label_4_3.grid(row=4, column=3)

label_4_4 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_4["font"] = myFont
label_4_4.grid(row=4, column=4)

label_4_5 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_5["font"] = myFont
label_4_5.grid(row=4, column=5)

label_4_6 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_6["font"] = myFont
label_4_6.grid(row=4, column=6)

label_4_7 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_4_7["font"] = myFont
label_4_7.grid(row=4, column=7)

#####################################################################

label_5_0 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_0["font"] = myFont
label_5_0.grid(row=5, column=0)

label_5_1 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_1["font"] = myFont
label_5_1.grid(row=5, column=1)

label_5_2 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_2["font"] = myFont
label_5_2.grid(row=5, column=2)

label_5_3 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_3["font"] = myFont
label_5_3.grid(row=5, column=3)

label_5_4 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_4["font"] = myFont
label_5_4.grid(row=5, column=4)

label_5_5 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_5["font"] = myFont
label_5_5.grid(row=5, column=5)

label_5_6 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_6["font"] = myFont
label_5_6.grid(row=5, column=6)

label_5_7 = tk.Button(
    master=frame_top,
    text="{}".format(randint(0, 5)),
    borderwidth=0,
    bg="black",
    fg="white",
)
label_5_7["font"] = myFont
label_5_7.grid(row=5, column=7)

#####################################################################


def changing_num(event=None):
    label_0_0.configure(text="{}".format(randint(0, 9)))
    label_0_1.configure(text="{}".format(randint(0, 9)))
    label_0_2.configure(text="{}".format(randint(0, 9)))
    label_0_3.configure(text="{}".format(randint(0, 9)))
    label_0_4.configure(text="{}".format(randint(0, 9)))
    label_0_5.configure(text="{}".format(randint(0, 9)))
    label_0_6.configure(text="{}".format(randint(0, 9)))
    label_0_7.configure(text="{}".format(randint(0, 9)))
    #####################################################################

    label_1_0.configure(text="{}".format(randint(0, 9)))
    label_1_1.configure(text="{}".format(randint(0, 9)))
    label_1_2.configure(text="{}".format(randint(0, 9)))
    label_1_3.configure(text="{}".format(randint(0, 9)))
    label_1_4.configure(text="{}".format(randint(0, 9)))
    label_1_5.configure(text="{}".format(randint(0, 9)))
    label_1_6.configure(text="{}".format(randint(0, 9)))
    label_1_7.configure(text="{}".format(randint(0, 9)))
    #####################################################################

    label_2_0.configure(text="{}".format(randint(0, 9)))
    label_2_1.configure(text="{}".format(randint(0, 9)))
    label_2_2.configure(text="{}".format(randint(0, 9)))
    if label_2_3["bg"] != "white":
        label_2_3.configure(text="{}".format(randint(0, 4)))

    if label_2_4["bg"] != "white":
        label_2_4.configure(text="{}".format(randint(0, 9)))
        if label_2_3["text"] == "5":
            label_2_4.configure(text="0")
        elif label_2_3["text"] == "0" and label_2_4["text"] == "0":
            label_2_4.configure(text="1")
        elif label_2_3["text"] == "4":
            label_2_4.configure(text="{}".format(randint(0, 3)))
        else:
            label_2_4.configure(text="{}".format(randint(0, 9)))

    label_2_5.configure(text="{}".format(randint(0, 9)))
    label_2_6.configure(text="{}".format(randint(0, 9)))
    label_2_7.configure(text="{}".format(randint(0, 9)))
    #####################################################################

    label_3_0.configure(text="{}".format(randint(0, 9)))
    label_3_1.configure(text="{}".format(randint(0, 9)))
    label_3_2.configure(text="{}".format(randint(0, 9)))
    label_3_3.configure(text="{}".format(randint(0, 9)))
    label_3_4.configure(text="{}".format(randint(0, 9)))
    label_3_5.configure(text="{}".format(randint(0, 9)))
    label_3_6.configure(text="{}".format(randint(0, 9)))
    label_3_7.configure(text="{}".format(randint(0, 9)))
    #####################################################################

    label_4_0.configure(text="{}".format(randint(0, 9)))
    label_4_1.configure(text="{}".format(randint(0, 9)))
    label_4_2.configure(text="{}".format(randint(0, 9)))
    label_4_3.configure(text="{}".format(randint(0, 9)))
    label_4_4.configure(text="{}".format(randint(0, 9)))
    label_4_5.configure(text="{}".format(randint(0, 9)))
    label_4_6.configure(text="{}".format(randint(0, 9)))
    label_4_7.configure(text="{}".format(randint(0, 9)))
    #####################################################################

    label_5_0.configure(text="{}".format(randint(0, 9)))
    label_5_1.configure(text="{}".format(randint(0, 9)))
    label_5_2.configure(text="{}".format(randint(0, 9)))
    label_5_3.configure(text="{}".format(randint(0, 9)))
    label_5_4.configure(text="{}".format(randint(0, 9)))
    label_5_5.configure(text="{}".format(randint(0, 9)))
    label_5_6.configure(text="{}".format(randint(0, 9)))
    label_5_7.configure(text="{}".format(randint(0, 9)))
    frame_top.after(200, changing_num)


changing_num()
frame_top.mainloop()
