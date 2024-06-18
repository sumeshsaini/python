import re
from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == '=':
        try:
            expression = nvalue.get()
            result = evaluate_expression(expression)
            nvalue.set(result)
        except Exception as e:
            nvalue.set("Error")
    elif text == 'AC':
        nvalue.set("")
    else:
        nvalue.set(nvalue.get() + text)

def evaluate_expression(expression):
    # Remove leading zeros from numbers in the expression
    expression = re.sub(r'\b0+(\d+)', r'\1', expression)
    try:
        return str(eval(expression))
    except Exception as e:
        return "Error"

root = Tk()
root.geometry("400x558")
root.maxsize(400,558)
root.minsize(400,558)
root.title("Calculator")

# Function to create buttons with styling
def create_button(frame, text, bg="lightgrey", fg="black", width=6, height=3):
    b = Button(frame, text=text, font="Arial 15 bold", width=width, height=height, bg=bg, fg=fg, bd=0)
    b.pack(side='left', padx=5, pady=5)
    b.bind("<Button-1>", click)

# Display Entry widget
nvalue = StringVar()
nvalue.set("")
Display = Entry(root, textvariable=nvalue, font="Arial 30 bold", bd=10, insertwidth=4, justify='right')
Display.pack(fill='x', ipadx=8, ipady=10, padx=10, pady=10)

# Frame for buttons
f = Frame(root, bg="black")
f.pack()

# Creating buttons
create_button(f, '7')
create_button(f, '8')
create_button(f, '9')
create_button(f, '/', bg="orange")

f = Frame(root, bg="black")
f.pack()

create_button(f, '4')
create_button(f, '5')
create_button(f, '6')
create_button(f, '*', bg="orange")

f = Frame(root, bg="black")
f.pack()

create_button(f, '1')
create_button(f, '2')
create_button(f, '3')
create_button(f, '-', bg="orange")

f = Frame(root, bg="black")
f.pack()

create_button(f, '0')
create_button(f, '+', bg="orange")
create_button(f, '=', bg="orange")
create_button(f, '.', bg="orange")


f = Frame(root, bg="black")
f.pack()

create_button(f, 'AC', bg="red", fg="white", width=14, height=3)

root.mainloop()




