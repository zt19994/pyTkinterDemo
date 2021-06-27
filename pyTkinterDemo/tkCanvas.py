#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 12:29
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('my title')
window.geometry('800x800')

# tk.Canvas()画布
canvas = tk.Canvas(window, bg='blue', height=500, width=800)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
canvas.pack()


# 移动函数，矩形向下移动2
def moveit():
    canvas.move(rect, 0, 2)


b = tk.Button(window, text='move', command=moveit).pack()

window.mainloop()
