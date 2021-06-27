#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 11:01
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('window')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


btn1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
btn1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))

# tk.Listbox() 列表选择
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()
