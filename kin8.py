from tkinter import *
root=Tk()
height = 400
base = 800
root.geometry(f"{base}x{height}")
canvass=Canvas(root,width=base,height=height)
canvass.pack()
canvass.create_line(0,0,800,400)
canvass.create_line(0,400,800,0)
canvass.create_rectangle(2,4,700,300)
root.mainloop()