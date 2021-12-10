import os
import tkinter as tk

def call_slr():
    os.system("python slr.py")
def call_clr():
    os.system("python clr.py")
def call_lalr():
    os.system("python lalr.py")
def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))