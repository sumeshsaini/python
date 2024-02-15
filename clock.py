import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")

# Create a label for the clock display
clock_label = tk.Label(root, font=('Arial', 40), bg='black', fg='white')
clock_label.pack(padx=50, pady=50)

# Update the clock display every second
update_clock()

# Run the Tkinter event loop
root.mainloop()
