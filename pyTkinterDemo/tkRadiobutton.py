#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 11:19
# @Author  : zt


import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())


# tk.Radiobutton() 单选
rl = tk.Radiobutton(window, text='OptionA', variable=var, value='A', command=print_selection)
rl.pack()
r2 = tk.Radiobutton(window, text='OptionB', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='OptionC', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()
