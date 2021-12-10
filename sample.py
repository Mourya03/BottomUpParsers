from re import sub
from tkinter import *
import tkinter as ttk

root = Tk()
root.geometry("200x150")
frm = ttk.Frame(root, padx=10,pady=10)
frm.pack()

ttk.Label(frm, text ="Hello!").pack()

my_entry = ttk.StringVar()
Entry(frm, width = 15, textvariable=my_entry).pack()
#my_entry.insert(0,'password')

def fun():
    print(my_entry.get(),type(my_entry.get()))
    ttk.Label(frm,text=my_entry.get(),background="white").pack()

ttk.Button(frm, text = "Submit", command = fun).pack()

ttk.Button(frm, text="Exit", command=root.destroy).pack()

lst=[1,2,3,4,5,6]

ttk.Label(frm,text=str(lst)).pack()

data = ttk.StringVar()
inp = ttk.Entry(frm,width=15,textvariable=data)
inp.pack()

def eval():
    ttk.Label(frm,text=data.get()).pack()

submt = ttk.Button(frm,command=eval)
submt.pack()


root.mainloop()

