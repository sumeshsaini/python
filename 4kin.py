from tkinter import*
def wish():
    print("Hello Boss")
def my():
    print("Whats up")
root=Tk()
root.geometry("655x333")
root.title("Button")
frame=Frame(root,bg='red',relief='groove',borderwidth=6)
frame.pack(side='top',padx=1,anchor='nw')
b = Button(frame,text="Select",width=15,height=3,fg='red',bg='black',command=wish)
b.pack(pady=5)
b2=Button(frame,text="OK",width=15,height=3,fg='red',bg='black',command=my)
b2.pack(pady=5)
root.mainloop()