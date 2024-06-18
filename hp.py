from tkinter import*  
root=Tk()
#creating a title
root.title("Management")
#creating the screen size
root.geometry("600x500")
root.maxsize(600,500)
root.minsize(600,500)
#creating labels
user=Label(text="Username").grid(row=0,column=0)
password=Label(text="Password").grid(row=1,column=0)
#creating button
Button(text="Submit").grid(row=2,column=2)
#creating var type
user_value=StringVar
pass_value=StringVar
#creating entry
user_entry=Entry(textvariable=user_value).grid(row=0,column=1)
pass_entry=Entry(textvariable=pass_value).grid(row=1,column=1)

root.mainloop()