__author__ = 'Ioan Balaban'
from tkinter import *
from functools import partial

def validateLogin(username, password):
    print("username entered : ", username.get())
    print("password entered : ", password.get())
    return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Logare cont')

#username label and text entry box
usernameLabel = Label(tkWindow, text = "User Name") .grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username) .grid(row=0, column=1)

#password
passwordLabel = Label(tkWindow, text = "Password") .grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable = password, show = '*') .grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#Login
loginButton = Button (tkWindow, text="Login", command=validateLogin, bg='#0052cc', width=20, fg='#ffffff') .grid(row=4, column=0)

tkWindow.mainloop()

