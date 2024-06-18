from tkinter import *

root = Tk()

root.geometry("700x500")

my = Scale(root,from_=0,to=10).pack()
my=Scale(root,from_=0,to=10,orient=HORIZONTAL).pack(anchor="nw")


root.mainloop()