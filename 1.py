from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
root = Tk()

def btn_clicky():
    info_str = 'Ванильное'
    showinfo(title='Вид мороженого', message=info_str)

def btn_clickb():
    info_str1 = 'Шоколадное'
    showinfo(title='Вид мороженого', message=info_str1)

def btn_clickbl():
    info_str2 = 'Крем-брюле'
    showinfo(title='Вид мороженого', message=info_str2)

def btn_clickg():
    info_str3 = 'Мятное'
    showinfo(title='Вид мороженого', message=info_str3)

root['bg'] = '#000000'
root.title('Кафе-мороженое')
root.wm_attributes('-alpha', 1)
root.geometry('200x200')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=200, width=200)
canvas.pack()

frame = Frame(root, bg='#BC8F8F')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Виды мороженого', bg='grey', font=40)
title.pack()
btn = Button(frame, text='Vanille', bg='white', command=btn_clicky)
btn.pack()

btn = Button(frame, text='Chocolate', bg='white', command=btn_clickb)
btn.pack()

btn = Button(frame, text='Creme brulee', bg='white', command=btn_clickbl)
btn.pack()

btn = Button(frame, text='Mint', bg='white', command=btn_clickg)
btn.pack()

root.mainloop()
