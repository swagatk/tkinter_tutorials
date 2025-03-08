import tkinter as tk
import ttkbootstrap as tb
from pathlib import Path
import csv
from dashboard import dashboard



# functions
def register():
    global reg_screen, username, password, lbl_error, lbl_success
    reg_screen = tb.Toplevel(root)
    reg_screen.title("Register")
    reg_screen.geometry("300x250")

    # set text variables
    username = tb.StringVar()
    password = tb.StringVar()

    lbl_un = tb.Label(reg_screen, text="Username*", bootstyle="warning", justify='center', )
    lbl_un.pack(padx=10, pady=10)
    entry_un = tb.Entry(reg_screen, textvariable=username)
    entry_un.pack(pady=10)

    lbl_pw = tb.Label(reg_screen, text="Password*", bootstyle="warning", justify='center')
    lbl_pw.pack()
    entry_pw = tb.Entry(reg_screen, textvariable=password, show="*")
    entry_pw.pack(pady=10)

    btn_frame = tb.Frame(reg_screen, border=True)
    btn_reg = tb.Button(btn_frame, text="Register", bootstyle="default", command=register_user)
    btn_reg.grid(row=0, column=0, padx=10, pady=10)
    btn_exit = tb.Button(btn_frame, text="Exit", bootstyle="danger", command=reg_screen.destroy)
    btn_exit.grid(row=0, column=1, padx=10, pady=10)
    btn_frame.pack()

    lbl_success = tb.Label(reg_screen, text="", bootstyle="success")
    lbl_success.pack()
    lbl_error = tb.Label(reg_screen, text="", bootstyle="danger")
    lbl_error.pack()

def register_user():
    global reg_screen, username, password
    if not username.get():
        lbl_error.config(text="Empty Username field!")
        lbl_success.config(text="")
    elif not password.get():
        lbl_error.config(text="Empty Password field!")
        lbl_success.config(text="")
    else:    
        filename = username.get() + '.txt'
        file_path = Path('./' + filename)
        if not file_path.exists():
            file = open(filename, "w")
            file.write(username.get() + "," + password.get() + "\n")
            file.close()
            lbl_success.config(text="Registration successful!")
            lbl_error.config(text="")
        else:
            lbl_success.config(text="")
            lbl_error.config(text="User already exists.")


def login():
    global login_screen, root, uname, passwd, lbl_login_error, lbl_login_success

    login_screen = tb.Toplevel(root)
    login_screen.title("Login Screen")
    login_screen.geometry("300x400")

    uname = tb.StringVar()
    passwd = tb.StringVar()

    lbl_un = tb.Label(login_screen, text="Username*", bootstyle="warning", justify='center', )
    lbl_un.pack(padx=10, pady=10)
    entry_un = tb.Entry(login_screen, textvariable=uname)
    entry_un.pack(pady=10)

    lbl_pw = tb.Label(login_screen, text="Password*", bootstyle="warning", justify='center')
    lbl_pw.pack()
    entry_pw = tb.Entry(login_screen, textvariable=passwd, show="*")
    entry_pw.pack(pady=10)

    btn_frame = tb.Frame(login_screen, border=True)
    btn_reg = tb.Button(btn_frame, text="Login", bootstyle="default", command=login_user)
    btn_reg.grid(row=0, column=0, padx=10, pady=10)
    btn_exit = tb.Button(btn_frame, text="Exit", bootstyle="danger", command=login_screen.destroy)
    btn_exit.grid(row=0, column=1, padx=10, pady=10)
    btn_frame.pack()

    lbl_login_success = tb.Label(login_screen, text="", bootstyle="success")
    lbl_login_success.pack()
    lbl_login_error = tb.Label(login_screen, text="", bootstyle="danger")
    lbl_login_error.pack()


def login_user():

    global login_screen, lbl_login_success, lbl_login_error, uname, passwd

    if not uname.get():
        lbl_login_error.config(text="Empty Username field!")
        lbl_login_success.config(text="")
    elif not passwd.get():
        lbl_error.config(text="Empty Password field!")
        lbl_success.config(text="")
    else:    
        filename = uname.get() + '.txt'
        file_path = Path('./' + filename)
        if file_path.exists():
            file = open(file_path, "r")
            data = list(csv.reader(file, delimiter=','))
            file.close()
            if data[0][1] == passwd.get():
                lbl_login_error.config(text="")
                lbl_login_success.config(text="Login Successful!")
                db = tb.Button(login_screen, text="Continue", bootstyle="success", command=call_dashboard)
                db.pack(padx=10, pady=10)
            else:
                lbl_login_error.config(text="Wrong Password")
                lbl_login_success.config(text="")
        else:
            lbl_login_error.config(text="Username does not exist")
            lbl_login_success.config(text="")


def call_dashboard():
    global login_screen
    if login_screen:
        login_screen.destroy()
    dashboard()
            





# Main Application window
root = tb.Window(themename="superhero")
root.title("Main Screen")




lbl = tb.Label(root, text="Smart Home Application", 
               bootstyle="primary", justify='center',
               font=("Calibri, 15"))
lbl.pack(padx=10, pady=10)
mf = tb.Frame(root, bootstyle="default")
b1 = tb.Button(mf, text="Login", bootstyle="warning", command=login)
b1.grid(row=0, column=0, padx=10, pady=10)

b2 = tb.Button(mf, text="Register", bootstyle="success", command=register)
b2.grid(row=0, column=1, padx=10, pady=10)

mf.pack(padx=10, pady=10)

b3 = tb.Button(root, text="Exit", bootstyle="danger", command=root.destroy)
b3.pack(padx=10, pady=10)

root.mainloop()