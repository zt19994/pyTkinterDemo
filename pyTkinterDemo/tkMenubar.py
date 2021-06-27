#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 20:42
# @Author  : zt

import tkinter as tk

window = tk.Tk()
window.title('my title')
window.geometry('300x300')

l = tk.Label(window, text='', bg='yellow')
l.pack()

counter = 0


def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1


# tk.Menu() 菜单
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(menubar, tearoff=0)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu1', command=do_job)

window.config(menu=menubar)
window.mainloop()
