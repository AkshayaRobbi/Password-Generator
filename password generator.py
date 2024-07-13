from tkinter import *
from tkinter import messagebox
import random
win=Tk()
win.title("Welcome to password generator")
win.geometry("1000x600")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')','-','_']
digits=['0','1','2','3','4','5','6','7','8','9']
title = Label(win, text="Welcome to Password Generator", font=("Times", 20))
title.pack(pady=10)
u_letters=Label(win,text="Enter the number of uppercase letters required in password",font=("Times",15))
u_letters.place(x=30,y=60)
l_entry=Entry(win,font=("Times",15))
l_entry.place(x=30,y=100)
n_letters=Label(win,text="Enter the number of letters required in password",font=("Times",15))
n_letters.place(x=30,y=140)
n_entry=Entry(win,font=("Times",15))
n_entry.place(x=30,y=180)
n_symbols=Label(win,text="Enter the number of symbols required in password",font=("Times",15))
n_symbols.place(x=30,y=220)
s_entry=Entry(win,font=("Times",15))
s_entry.place(x=30,y=260)
n_digits=Label(win,text="Enter the number of digits required in password",font=("Times",15))
n_digits.place(x=30,y=300)
d_entry=Entry(win,font=("Times",15))
d_entry.place(x=30,y=340)
password=Label(win,text="Your password is :",font=("Times",15))
password.place(x=300,y=450)
pwd_entry=Entry(win,font=("Times",15))
pwd_entry.place(x=450,y=450)
def generate_password():
    try:
        u_count = int(l_entry.get())
        n_count = int(n_entry.get())
        s_count = int(s_entry.get())
        d_count = int(d_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for each field.")
        return
    password_list=[]
    for i in range(u_count):
        c=random.choice(letters)
        password_list.extend(c.upper())
    for i in range(n_count):
        c=random.choice(letters)
        password_list.extend(c)
    for i in range(s_count):
        c=random.choice(symbols)
        password_list.extend(c)
    for i in range(d_count):
        c=random.choice(digits)
        password_list.extend(c)
    random.shuffle(password_list)
    password_str=""
    for i in password_list:
        password_str+=i;
    pwd_entry.delete(0,END)
    pwd_entry.insert(0,password_str)
generate_password=Button(win,text="Generate Password",command=generate_password,font=("Times",15))
generate_password.place(x=400,y=380)

win.mainloop()

