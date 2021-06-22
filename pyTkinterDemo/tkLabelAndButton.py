#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 23:27
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('window')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set("")


btn = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
btn.pack()

window.mainloop()
