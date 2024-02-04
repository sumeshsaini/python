from tkinter import*
ok_root=Tk()
ok_root.geometry("700x500")
#lock the minimum size
ok_root.minsize(300,250)
#lock the maximum size
ok_root.maxsize(900,900)
#create a label
call=Label(text="Welcome to real world")
call.pack()
ok_root.mainloop()