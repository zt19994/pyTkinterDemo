#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 21:13
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('window')
window.geometry('200x200')

# tk.Entry() 输入框，show='*' 显示为*号
e = tk.Entry(window, show=None)
e.pack()


# 在指针处插入
# t.insert(1.1, var)  在第一行第二列插入 列从0开始
def insert_point():
    var = e.get()
    t.insert(1.1, var)


# 在尾部插入
def insert_end():
    var = e.get()
    t.insert('end', var)


btn1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
btn1.pack()
btn2 = tk.Button(window, text='insert end', command=insert_end)
btn2.pack()

# tk.Text() 文本框
t = tk.Text(window, height=2)
t.pack()

window.mainloop()
