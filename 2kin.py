from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("My GUI")
call=Label(text='''Welcome''',bg="black",fg="white",padx=10,pady=100, font=("comicsansms",19,"bold"),
           borderwidth=14,relief=GROOVE)
call.pack(side=TOP,anchor="center",fill=X)
root.mainloop()