from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    date = strftime('%A, %B %d, %Y')
    label.config(text=string)
    date_label.config(text=date)
    label.after(1000, time)

label = Label(root, font=('ds-digital', 100), background="black", foreground="cyan")
label.pack(anchor='center')

date_label = Label(root,font=('Helvetica', 54),background="black",foreground="ghostwhite",borderwidth=10,relief="ridge")
date_label.pack()

time()
mainloop()
