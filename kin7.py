from tkinter import *
def give():
    print("Submiting your form")
    data=print(f"{namevalue.get()}, {contact_value.get()}, {gender_value.get()}, {emergency_value.get()}, {pay_value.get()}, {food.get()}")
root=Tk()
root.geometry("634x333")
root.title("RECORD")
Label(root,text="Welcome to the form",font=("comicsansms",15,"bold"),pady=15).grid(row=0,column=3)
name = Label(root,text="Name").grid(row=1,column=2)
contact = Label(root,text="Contact number").grid(row=2,column=2)
gender = Label(root,text="Gender").grid(row=3,column=2)
emergency=Label(root,text="Emergency number").grid(row=4,column=2)
pay = Label(root,text="Payment").grid(row=5,column=2)
namevalue=StringVar()
contact_value=StringVar()
gender_value=StringVar()
emergency_value=StringVar()
pay_value=StringVar()
food=IntVar()
name_entry=Entry(root,textvariable=namevalue).grid(row=1,column=3)
contact_entry=Entry(root,textvariable=contact_value).grid(row=2,column=3)
gender_entry=Entry(root,textvariable=gender_value).grid(row=3,column=3)
emergency_entry=Entry(root,textvariable=emergency_value).grid(row=4,column=3)
pay_entry=Entry(root,textvariable=pay_value).grid(row=5,column=3)
food_value=Checkbutton(root,text="Do you need food service",variable=food)
food_value.grid(row=6,column=3)
Button(root,text="Submit",command=give).grid(row=7,column=3)
root.mainloop()