#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 21:24
# @Author  : zt
import pickle
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my title')
window.geometry('550x400')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name:').place(x=100, y=200)
tk.Label(window, text='Password:').place(x=100, y=240)

var_user_name = tk.StringVar()
var_user_name.set('example@tkinter.com')
var_user_pwd = tk.StringVar()
# user entry
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=210, y=200)
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, show='*')
entry_user_pwd.place(x=210, y=240)


def user_login():
    usr_name = var_user_name.get()
    usr_pwd = var_user_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you?' + usr_name)
        else:
            tk.messagebox.showinfo(message='Error,your password is wrong, try again')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not sign up yet. Sign up today')

        if is_sign_up:
            user_sign_up()


def user_sign_up():
    def sign_to_web():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('Sign up window')
    window_sign_up.geometry('350x300')

    new_name = tk.StringVar()
    new_name.set("example@tkinter.com")
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=50)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=50)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=90)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=90)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=130)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=130)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_web)
    btn_confirm_sign_up.place(x=170, y=180)


# login and sign up button
btn_login = tk.Button(window, text='Login', command=user_login)
btn_login.place(x=220, y=280)
btn_sign_up = tk.Button(window, text='Sign up', command=user_sign_up)
btn_sign_up.place(x=270, y=280)

window.mainloop()
