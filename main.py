from functions import *
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("500x500")
root.title("Bottom-Up Parsers")
root.config(bg='#D9D8D7')
style = ttk.Style(root)

frame = tk.Frame(root, padx=10,pady=10,bg='#D9D8D7')
frame.pack()

slr_btn = tk.Button(frame,width=20,font=('calibri', 20, 'bold'),bd=10,bg="#4a7abc",foreground = 'white smoke',text = "SLR Parser",command=call_slr,cursor="hand2")
clr_btn = tk.Button(frame,width=20,font=('calibri', 20, 'bold'),bd=10,bg="#4a7abc",foreground = 'white smoke',text = "CLR Parser",command=call_clr,cursor="hand2")
lalr_btn = tk.Button(frame,width=20,font=('calibri', 20, 'bold'),bd=10,bg="#4a7abc",foreground = 'white smoke',text = "LALR Parser",command=call_lalr,cursor="hand2")
exit_btn = tk.Button(frame,width=10,font=('calibri', 20, 'bold'),bd=10,bg="#D9290e",foreground = 'white smoke',text = "CLOSE",command=root.destroy,cursor="hand2")

tk.Label(frame,text="BOTTOM UP PARSERS",foreground="black",bg='#D9D8D7',pady=20,font=('ariel', 30, 'bold','underline')).pack()
slr_btn.pack()
tk.Label(frame,text=" ",bg='#D9D8D7').pack()
clr_btn.pack()
tk.Label(frame,text=" ",bg='#D9D8D7').pack()
lalr_btn.pack()
tk.Label(frame,text=" ",bg='#D9D8D7').pack()
exit_btn.pack()

changeOnHover(slr_btn, "blue","#4a7abc")
changeOnHover(clr_btn, "blue","#4a7abc")
changeOnHover(lalr_btn, "blue","#4a7abc")
changeOnHover(exit_btn, "red","#D9290e")

root.mainloop()