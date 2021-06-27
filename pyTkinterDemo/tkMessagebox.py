#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 21:02
# @Author  : zt

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my title')
window.geometry('300x300')


def hit_me():
    # tk.messagebox.showinfo(title='Hi', message='hahahaha')
    # tk.messagebox.showwarning(title='Hi', message='nonono')
    # tk.messagebox.showerror(title='Hi', message='No!!never')
    # print(tk.messagebox.askquestion(title='Hi', message='No!!never'))  # return yes no
    # print(tk.messagebox.askyesno(title='Hi', message='No!!never'))  # return True False
    # print(tk.messagebox.askretrycancel(title='Hi', message='No!!never'))  # return True False
    print(tk.messagebox.askokcancel(title='Hi', message='No!!never'))  # return True False


tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
