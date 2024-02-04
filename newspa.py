import tkinter
from tkinter import PhotoImage
from tkinter import*
root=Tk()
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.title("News Paper")
c=Label(text="News Paper",bg="blue",fg="red",font=("comicsansms",20,"bold","italic"),
        borderwidth=8,relief="groove")
image_path=PhotoImage(file=r"C:\Users\Sumesh Saini\Pictures\newspaper-icon-28.png")
c.pack(side="top",fill=X)
bimage =tkinter.Label(root,image=image_path)
bimage.pack()
mainloop()