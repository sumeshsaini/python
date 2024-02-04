from tkinter import*
def wish():
    print("Hello Boss")
root=Tk()
root.geometry("655x333")
root.title("Button")
frame=Frame(root,bg='red',relief='groove',borderwidth=6)
frame.pack(side='top',padx=1,anchor='nw')
b = Button(frame,text="Select",fg='red',bg='black',command=wish)
b.pack()
root.mainloop()