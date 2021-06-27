#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 21:16
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('my title')
window.geometry('300x300')

# pack() 放置
# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

# grid() 网格布局
# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

tk.Label(window, text=1).place(x=10, y=100, anchor='center')

window.mainloop()
