from tkinter import *
from tkinter import ttk

expr=""

def press(key):
    global expr
    expr +=str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        #expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")


if __name__ == "__main__":
    root = Tk()
    root.title('Calculator')
    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=7, ipadx=90)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="1", command=lambda: press(1)).grid(column=1, row=0)
    ttk.Button(frm, text="2", command= lambda: press(2)).grid(column=2, row =0)
    ttk.Button(frm, text="3", command=lambda: press(3)).grid(column=3, row=0)
    ttk.Button(frm, text="4", command= lambda: press(4)).grid(column=1, row =1)
    ttk.Button(frm, text="5", command=lambda: press(5)).grid(column=2, row=1)
    ttk.Button(frm, text="6", command= lambda: press(6)).grid(column=3, row =1)
    ttk.Button(frm, text="7", command=lambda: press(7)).grid(column=1, row=2)
    ttk.Button(frm, text="8", command= lambda: press(8)).grid(column=2, row =2)
    ttk.Button(frm, text="9", command=lambda: press(9)).grid(column=3, row=2)
    ttk.Button(frm, text="Clear", command=clear).grid(column=2, row=3)
    ttk.Button(frm, text="0", command= lambda: press(0)).grid(column=1, row =3)
    ttk.Button(frm, text="=", command=equal).grid(column=3, row =3)
    ttk.Button(frm, text="+", command=lambda: press('+')).grid(column=4, row=0)
    ttk.Button(frm, text="-", command= lambda: press('-')).grid(column=4, row =1)
    ttk.Button(frm, text="/", command=lambda: press('/')).grid(column=4, row=2)
    ttk.Button(frm, text="*", command= lambda: press('*')).grid(column=4, row =3)
    ttk.Button(frm, text=".", command= lambda: press('.')).grid(column=1, row =4)
    root.mainloop()    