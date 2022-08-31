# -*- coding : cp949 -*-
from tkinter import *
from random import randint
import tkinter.font as font


class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        # ----- myContainer1 -----
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.clicked_num = 0
        self.clicked_num2 = 0
        self.final_num = ""
        # self.inner_button = [['button_0_0', 'button_1_0', 'button_2_0', 'button_3_0', 'button_4_0', 'button_5_0', ],
        #                      ['button_0_2', 'button_1_2', 'button_2_2',
        #                       'button_3_2', 'button_4_2', 'button_5_2', ],
        #                      ['button_0_3', 'button_1_3', 'button_2_3',
        #                       'button_3_3', 'button_4_3', 'button_5_3', ],
        #                      ['button_0_4', 'button_1_4', 'button_2_4',
        #                       'button_3_4', 'button_4_4', 'button_5_4', ],
        #                      ['button_0_1', 'button_1_1', 'button_2_1',
        #                       'button_3_1', 'button_4_1', 'button_5_1', ],
        #                      ['button_0_5', 'button_1_5', 'button_2_5', 'button_3_5', 'button_4_5', 'button_5_5', ], ]

        # ----- 조감을 제어하는에 필요한 상수들 -----        
        button_width = 6
        # button_padx = "2m"
        # button_pady = "1m"
        # buttons_frame_padx = "3m"
        # buttons_frame_pady = "2m"
        # buttons_frame_ipadx = "3m"
        # buttons_frame_ipady = "1m"
        # ----- 상수 끝 -----     

        # ### myContainer1안에 수직적 동선을 사용한다.        
        # ### myContainer1안에 먼저 buttons_frame을 만든 후        
        # ### top_frame와 bottom_frame를 만든다  

        # # ----- buttons_frame -----        
        self.buttons_frame = Frame(self.myContainer1, background="blue")
        self.buttons_frame.pack(side=TOP)

        #  버튼들을 buttons_frame에 추가한다.       

        # # ----- button1 -----        
        self.button1 = Button(self.buttons_frame, command=self.button1Click)
        self.button1.bind("<Return>", self.button1Click)
        self.button1.configure(text="".format(self.clicked_num), background="green",
                               width=button_width)
        self.button1.focus_force()  # 초기 초점 지정        
        self.button1.pack(side=LEFT)

        # ----- button2 -----        
        self.button0 = Button(self.buttons_frame, command=self.button0Click)
        self.button0.bind("<Return>", self.button0Click)
        self.button0.configure(text="Cancel", background="red",
                               width=button_width)
        self.button0.pack(side=RIGHT)

        # ----- top_frame -----        
        self.top_frame = Frame(self.myContainer1)
        self.top_frame.pack(side=TOP,
                            fill=BOTH,
                            expand=YES)
        # ----- bottom_frame -----        
        self.bottom_frame = Frame(self.myContainer1,
                                  borderwidth=5,                                 # 틀 테두리 두꼐
                                  relief=RIDGE,  # 틀 모양                                
                                  height=50,  # 틀 높이                                
                                  background="white")
        self.bottom_frame.pack(side=TOP,
                               fill=BOTH,  # 빈공간 채우기                               
                               expand=YES)
        # left_frame과 right_frame이라는        
        # ### 두개의 틀을 top_frame안에 배치한다.        
        # ### top_frame안에 수평적동선을 사용한다.               
        #
        # # ----- left_frame -----        
        self.left_frame = Frame(self.top_frame,
                                background="black",
                                borderwidth=5,
                                relief=RIDGE,
                                height=150,
                                width=550)

        self.left_frame.pack(side=LEFT,)

        # inner button of left frame
        myFont = font.Font(size=20, family='Helvetica')

        # for row in range(6):
        #     for col in range(6):
        #         random_int = randint(0, 9)
        #         self.inner_button[row][col] = Button(
        #             self.left_frame, command=lambda random_int=random_int: self.set_var(random_int))
        #         self.inner_button[row][col].bind("<Return>", self.button1Click)
        #         self.inner_button[row][col].configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
        #                                               width=10, height=5)
        #         self.inner_button[row][col]['font'] = myFont
        #         # self.inner_button.focus_force()  # 초기 초점 지정        
        #         self.inner_button[row][col].grid(row=row, column=col)

        # for row in range(6):
        #     for col in range(6):
        #         random_int = randint(0, 9)
        #         print(self.inner_button[row][col])
        #         self.inner_button[row][col] = Button(
        #             self.left_frame, command=self.button1Click)
        #         print(self.inner_button[row][col])

        #         self.inner_button[row][col].bind("<Return>", self.button1Click)
        #         self.inner_button[row][col].configure(text="{}".format(self.inner_button[row][col]), background="black", fg='white', borderwidth=0,
        #                                               width=10, height=5)
        #         self.inner_button[row][col]['font'] = myFont
        #         self.inner_button[row][col].focus_force()  # 초기 초점 지정        
        #         self.inner_button[row][col].grid(row=row, column=col)

        random_int = randint(0, 9)

        self.inner_button_0_0 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_0_0.bind("<Return>", self.button1Click)
        self.inner_button_0_0.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=0, height=5, padx=0, pady=0)
        self.inner_button_0_0['font'] = myFont
        self.inner_button_0_0.grid(row=0, column=0)

        random_int = randint(0, 9)
        self.inner_button_0_1 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_0_1.bind("<Return>", self.button1Click)
        self.inner_button_0_1.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_0_1['font'] = myFont
        self.inner_button_0_1.grid(row=0, column=1)

        random_int = randint(0, 9)
        self.inner_button_0_2 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_0_2.bind("<Return>", self.button1Click)
        self.inner_button_0_2.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_0_2['font'] = myFont
        self.inner_button_0_2.grid(row=0, column=2)

        random_int = randint(0, 9)
        self.inner_button_0_3 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_0_3.bind("<Return>", self.button1Click)
        self.inner_button_0_3.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_0_3['font'] = myFont
        self.inner_button_0_3.grid(row=0, column=3)

        random_int = randint(0, 9)
        self.inner_button_0_4 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_0_4.bind("<Return>", self.button1Click)
        self.inner_button_0_4.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_0_4['font'] = myFont
        self.inner_button_0_4.grid(row=0, column=4)

        random_int = randint(0, 9)
        self.inner_button_0_5 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_0_5.bind("<Return>", self.button1Click)
        self.inner_button_0_5.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_0_5['font'] = myFont
        self.inner_button_0_5.grid(row=0, column=5)

        random_int = randint(0, 9)
        self.inner_button_1_0 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_1_0.bind("<Return>", self.button1Click)
        self.inner_button_1_0.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_1_0['font'] = myFont
        self.inner_button_1_0.grid(row=1, column=0)

        random_int = randint(0, 9)
        self.inner_button_1_1 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_1_1.bind("<Return>", self.button1Click)
        self.inner_button_1_1.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_1_1['font'] = myFont
        self.inner_button_1_1.grid(row=1, column=1)

        random_int = randint(0, 9)
        self.inner_button_1_2 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_1_2.bind("<Return>", self.button1Click)
        self.inner_button_1_2.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_1_2['font'] = myFont
        self.inner_button_1_2.grid(row=1, column=2)

        random_int = randint(0, 9)
        self.inner_button_1_3 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_1_3.bind("<Return>", self.button1Click)
        self.inner_button_1_3.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_1_3['font'] = myFont
        self.inner_button_1_3.grid(row=1, column=3)

        random_int = randint(0, 9)
        self.inner_button_1_4 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_1_4.bind("<Return>", self.button1Click)
        self.inner_button_1_4.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_1_4['font'] = myFont
        self.inner_button_1_4.grid(row=1, column=4)

        random_int = randint(0, 9)
        self.inner_button_1_5 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_1_5.bind("<Return>", self.button1Click)
        self.inner_button_1_5.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_1_5['font'] = myFont
        self.inner_button_1_5.grid(row=1, column=5)

        random_int = randint(0, 9)
        self.inner_button_2_0 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_2_0.bind("<Return>", self.button1Click)
        self.inner_button_2_0.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_2_0['font'] = myFont
        self.inner_button_2_0.grid(row=2, column=0)

        random_int = randint(0, 9)
        self.inner_button_2_1 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_2_1.bind("<Return>", self.button1Click)
        self.inner_button_2_1.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_2_1['font'] = myFont
        self.inner_button_2_1.grid(row=2, column=1)

        random_int = randint(0, 9)
        self.inner_button_2_2 = Button(
            self.left_frame, command=self.button2Click)

        self.inner_button_2_2.bind("<Return>", self.button2Click)
        self.inner_button_2_2.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_2_2['font'] = myFont
        self.inner_button_2_2.focus_force()  # 초기 초점 지정        
        self.inner_button_2_2.grid(row=2, column=2)

        random_int = randint(0, 9)
        self.inner_button_2_3 = Button(
            self.left_frame, command=self.button3Click)

        self.inner_button_2_3.bind("<Return>", self.button3Click)
        self.inner_button_2_3.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_2_3['font'] = myFont
        self.inner_button_2_3.focus_force()  # 초기 초점 지정        
        self.inner_button_2_3.grid(row=2, column=3)

        random_int = randint(0, 9)
        self.inner_button_2_4 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_2_4.bind("<Return>", self.button1Click)
        self.inner_button_2_4.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_2_4['font'] = myFont
        self.inner_button_2_4.grid(row=2, column=4)

        random_int = randint(0, 9)
        self.inner_button_2_5 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_2_5.bind("<Return>", self.button1Click)
        self.inner_button_2_5.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_2_5['font'] = myFont
        self.inner_button_2_5.grid(row=2, column=5)

        random_int = randint(0, 9)
        self.inner_button_3_0 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_3_0.bind("<Return>", self.button1Click)
        self.inner_button_3_0.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_3_0.grid(row=3, column=0)

        random_int = randint(0, 9)
        self.inner_button_3_1 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_3_1.bind("<Return>", self.button1Click)
        self.inner_button_3_1.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_3_1['font'] = myFont
        self.inner_button_3_1.grid(row=3, column=1)

        random_int = randint(0, 9)
        self.inner_button_3_2 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_3_2.bind("<Return>", self.button1Click)
        self.inner_button_3_2.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_3_2['font'] = myFont
        self.inner_button_3_2.grid(row=3, column=2)

        random_int = randint(0, 9)
        self.inner_button_3_3 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_3_3.bind("<Return>", self.button1Click)
        self.inner_button_3_3.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_3_3['font'] = myFont
        self.inner_button_3_3.grid(row=3, column=3)

        random_int = randint(0, 9)
        self.inner_button_3_4 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_3_4.bind("<Return>", self.button1Click)
        self.inner_button_3_4.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_3_4['font'] = myFont
        self.inner_button_3_4.grid(row=3, column=4)

        random_int = randint(0, 9)
        self.inner_button_3_5 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_3_5.bind("<Return>", self.button1Click)
        self.inner_button_3_5.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_3_5['font'] = myFont
        self.inner_button_3_5.grid(row=3, column=5)

        random_int = randint(0, 9)
        self.inner_button_4_0 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_4_0.bind("<Return>", self.button1Click)
        self.inner_button_4_0.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_4_0['font'] = myFont
        self.inner_button_4_0.focus_force()  # 초기 초점 지정        
        self.inner_button_4_0.grid(row=4, column=0)

        random_int = randint(0, 9)
        self.inner_button_4_1 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_4_1.bind("<Return>", self.button1Click)
        self.inner_button_4_1.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_4_1['font'] = myFont
        self.inner_button_4_1.grid(row=4, column=1)

        random_int = randint(0, 9)
        self.inner_button_4_2 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_4_2.bind("<Return>", self.button1Click)
        self.inner_button_4_2.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_4_2.grid(row=4, column=2)

        random_int = randint(0, 9)
        self.inner_button_4_3 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_4_3.bind("<Return>", self.button1Click)
        self.inner_button_4_3.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_4_3['font'] = myFont
        self.inner_button_4_3.grid(row=4, column=3)

        random_int = randint(0, 9)
        self.inner_button_4_4 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_4_4.bind("<Return>", self.button1Click)
        self.inner_button_4_4.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_4_4['font'] = myFont
        self.inner_button_4_4.grid(row=4, column=4)

        random_int = randint(0, 9)
        self.inner_button_4_5 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_4_5.bind("<Return>", self.button1Click)
        self.inner_button_4_5.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_4_5['font'] = myFont
        self.inner_button_4_5.grid(row=4, column=5)

        random_int = randint(0, 9)
        self.inner_button_5_0 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_5_0.bind("<Return>", self.button1Click)
        self.inner_button_5_0.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_5_0['font'] = myFont
        self.inner_button_5_0.grid(row=5, column=0)

        random_int = randint(0, 9)
        self.inner_button_5_1 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_5_1.bind("<Return>", self.button1Click)
        self.inner_button_5_1.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_5_1['font'] = myFont
        self.inner_button_5_1.grid(row=5, column=1)

        random_int = randint(0, 9)
        self.inner_button_5_2 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_5_2.bind("<Return>", self.button1Click)
        self.inner_button_5_2.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_5_2['font'] = myFont
        self.inner_button_5_2.grid(row=5, column=2)

        random_int = randint(0, 9)
        self.inner_button_5_3 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_5_3.bind("<Return>", self.button1Click)
        self.inner_button_5_3.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_5_3['font'] = myFont
        self.inner_button_5_3.grid(row=5, column=3)

        random_int = randint(0, 9)
        self.inner_button_5_4 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_5_4.bind("<Return>", self.button1Click)
        self.inner_button_5_4.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_5_4['font'] = myFont
        self.inner_button_5_4.grid(row=5, column=4)

        random_int = randint(0, 9)
        self.inner_button_5_5 = Button(
            self.left_frame, command=self.button1Click)

        self.inner_button_5_5.bind("<Return>", self.button1Click)
        self.inner_button_5_5.configure(text="{}".format(random_int), background="black", fg='white', borderwidth=0,
                                        width=10, height=5)
        self.inner_button_5_5['font'] = myFont
        self.inner_button_5_5.grid(row=5, column=5)

        # ----- right_frame -----        
        self.right_frame = Frame(self.top_frame,
                                 background="tan",
                                 borderwidth=5,
                                 relief=RIDGE,
                                 width=850)

        self.right_frame.pack(side=RIGHT,
                              fill=BOTH,
                              expand=YES)

        # -----inner frame of right frame -----
        self.inner_frame_of_right_frame = Frame(self.right_frame,
                                                borderwidth=5,
                                                relief=RIDGE,
                                                width=200,
                                                height=200)
        self.inner_frame_of_right_frame.place(relx=.5, rely=.5, anchor=CENTER)
        # -----label of inner frmae -----
        self.label_of_inner_frame = Label(self.inner_frame_of_right_frame,
                                          text="",
                                          background='white',
                                          width=200,
                                          height=200)
        self.label_of_inner_frame.place(relx=.5, rely=.5, anchor=CENTER)
    # ----- Functions -----    

    def button1Click(self, event=None):
        if self.inner_button["background"] == "green":
            self.inner_button.configure(background="yellow")
            self.clicked_num = self.inner_button['text']
        else:
            self.inner_button.configure(background="green")

    def button2Click(self, event=None):
        self.inner_button_2_2.configure(background='white', fg='black')
        self.clicked_num = self.inner_button_2_2['text']
        print(self.clicked_num)

    def button3Click(self, event=None):
        self.inner_button_2_3.configure(background='white', fg='black')
        self.clicked_num2 = self.inner_button_2_3['text']
        print(self.clicked_num2)
        myFont2 = font.Font(size=20, weight='bold', family='Helvetica')
        self.label_of_inner_frame['font'] = myFont2

        self.label_of_inner_frame.configure(
            background='black', fg='white', text='{}{}'.format(self.clicked_num, self.clicked_num2))
        self.final_num = str(self.clicked_num) + str(self.clicked_num2)
        print(self.final_num)
    # def set_var(self, var, event=None):
    #     self.clicked_num = var
    #     print(self.inner_button)

    # 어플리케이션 닫기

    def button0Click(self, event=None):
        self.myParent.destroy()

    def changing_num(self, event=None):
        self.inner_button_0_0.configure(text="{}".format(randint(0, 9)))
        self.inner_button_1_0.configure(text="{}".format(randint(0, 9)))
        self.inner_button_2_0.configure(text="{}".format(randint(0, 9)))
        self.inner_button_3_0.configure(text="{}".format(randint(0, 9)))
        self.inner_button_4_0.configure(text="{}".format(randint(0, 9)))
        self.inner_button_5_0.configure(text="{}".format(randint(0, 9)))
        self.inner_button_0_1.configure(text="{}".format(randint(0, 9)))
        self.inner_button_1_1.configure(text="{}".format(randint(0, 9)))
        self.inner_button_2_1.configure(text="{}".format(randint(0, 9)))
        self.inner_button_3_1.configure(text="{}".format(randint(0, 9)))
        self.inner_button_4_1.configure(text="{}".format(randint(0, 9)))
        self.inner_button_5_1.configure(text="{}".format(randint(0, 9)))
        self.inner_button_0_2.configure(text="{}".format(randint(0, 9)))
        self.inner_button_1_2.configure(text="{}".format(randint(0, 9)))
        if self.inner_button_2_2['background'] != 'white':
            self.inner_button_2_2.configure(text="{}".format(randint(0, 5)))
        self.inner_button_3_2.configure(text="{}".format(randint(0, 9)))
        self.inner_button_4_2.configure(text="{}".format(randint(0, 9)))
        self.inner_button_5_2.configure(text="{}".format(randint(0, 9)))
        self.inner_button_0_3.configure(text="{}".format(randint(0, 9)))
        self.inner_button_1_3.configure(text="{}".format(randint(0, 9)))
        if self.inner_button_2_3['background'] != 'white':
            self.inner_button_2_3.configure(text="{}".format(randint(0, 9)))
            if self.inner_button_2_2['text'] == "5":
                self.inner_button_2_3.configure(text="0")
        self.inner_button_3_3.configure(text="{}".format(randint(0, 9)))
        self.inner_button_4_3.configure(text="{}".format(randint(0, 9)))
        self.inner_button_5_3.configure(text="{}".format(randint(0, 9)))
        self.inner_button_0_4.configure(text="{}".format(randint(0, 9)))
        self.inner_button_1_4.configure(text="{}".format(randint(0, 9)))
        self.inner_button_2_4.configure(text="{}".format(randint(0, 9)))
        self.inner_button_3_4.configure(text="{}".format(randint(0, 9)))
        self.inner_button_4_4.configure(text="{}".format(randint(0, 9)))
        self.inner_button_5_4.configure(text="{}".format(randint(0, 9)))
        self.inner_button_0_5.configure(text="{}".format(randint(0, 9)))
        self.inner_button_1_5.configure(text="{}".format(randint(0, 9)))
        self.inner_button_2_5.configure(text="{}".format(randint(0, 9)))
        self.inner_button_3_5.configure(text="{}".format(randint(0, 9)))
        self.inner_button_4_5.configure(text="{}".format(randint(0, 9)))
        self.inner_button_5_5.configure(text="{}".format(randint(0, 9)))

        self.myParent.after(200, self.changing_num)


root = Tk()
myapp = MyApp(root)
myapp.changing_num()
root.mainloop()
