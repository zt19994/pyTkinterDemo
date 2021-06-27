#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 11:59
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('my title')
window.geometry('300x300')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')


var1 = tk.IntVar()
var2 = tk.IntVar()
# tk.Checkbutton() onvalue选择是数字 offvalue未选择时数字
cb1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
cb2 = tk.Checkbutton(window, text='C ++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
cb1.pack()
cb2.pack()

window.mainloop()
