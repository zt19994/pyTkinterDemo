#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 11:41
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have selected ' + v)


# tk.Scale() 滑动条 orient方向 showvalue是否显示数值在滑动条上面  tickinterval隔多少数值显示 resolution保留小数位
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             len=200, showvalue=0, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
