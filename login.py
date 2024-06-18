import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as tmsg
from tkinter import PhotoImage
import cv2
import os
from datetime import datetime
guests =  []
doctors = []
staff_list = []
patients = []

def capture():   #evidence
    # Open the default camera (usually the first one available)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Capture a single frame from the camera
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Close OpenCV window
    cv2.destroyAllWindows()

    # Check if the frame is captured successfully
    if ret:
        # Define the path to save the photo
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        photo_path = os.path.join(desktop_path, 'captured_photo.jpg')

        # Save the captured frame as a photo
        cv2.imwrite(photo_path, frame)
        
    else:
        print("Error: Failed to capture photo.")


#patient

def add_patient():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    room_number = room_entry.get()
    problem = problem_entry.get()
    emergency_contact = emergency_entry.get()

    if name and age and address and room_number and problem and emergency_contact:
        patient_info = {
            "Name": name,
            "Age": age,
            "Address": address,
            "Room Number": room_number,
            "Problem": problem,
            "Emergency Contact": emergency_contact
        }
        patients.append(patient_info)
        messagebox.showinfo("Success", "Patient added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_patient():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del patients[index]
        messagebox.showinfo("Success", "Patient deleted successfully.")
        display_patients()
    else:
        messagebox.showerror("Error", "Please select a patient to delete.")

def display_patients():
    listbox.delete(0, tk.END)
    for patient in patients:
        listbox.insert(tk.END, f"Name: {patient['Name']}, Age: {patient['Age']}, Address: {patient['Address']}, Room Number: {patient['Room Number']}, Problem: {patient['Problem']}, Emergency Contact: {patient['Emergency Contact']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    room_entry.delete(0, tk.END)
    problem_entry.delete(0, tk.END)
    emergency_entry.delete(0, tk.END)

def patient_management():
    global name_entry, age_entry, address_entry, room_entry, problem_entry, emergency_entry, listbox

    patient_screen = tk.Tk()
    patient_screen.title("Patient Management")
    patient_screen.geometry("600x400")
    patient_screen.maxsize(600, 400)
    patient_screen.minsize(600, 400)
    patient_screen.configure(bg="#333333")

    tk.Label(patient_screen, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(patient_screen)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(patient_screen, text="Age:").grid(row=1, column=0, padx=5, pady=5)
    age_entry = tk.Entry(patient_screen)
    age_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(patient_screen, text="Address:").grid(row=2, column=0, padx=5, pady=5)
    address_entry = tk.Entry(patient_screen)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(patient_screen, text="Room Number:").grid(row=3, column=0, padx=5, pady=5)
    room_entry = tk.Entry(patient_screen)
    room_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(patient_screen, text="Problem:").grid(row=4, column=0, padx=5, pady=5)
    problem_entry = tk.Entry(patient_screen)
    problem_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(patient_screen, text="Emergency Contact:").grid(row=5, column=0, padx=5, pady=5)
    emergency_entry = tk.Entry(patient_screen)
    emergency_entry.grid(row=5, column=1, padx=5, pady=5)

    add_button = tk.Button(patient_screen, text="Add Patient", command=add_patient)
    add_button.grid(row=6, column=0, columnspan=2, pady=5)

    delete_button = tk.Button(patient_screen, text="Delete Patient", command=delete_patient)
    delete_button.grid(row=7, column=0, columnspan=2, pady=5)

    display_button = tk.Button(patient_screen, text="Display Patients", command=display_patients)
    display_button.grid(row=8, column=0, columnspan=2, pady=5)

    exit_button = tk.Button(patient_screen, text="Exit", command=patient_screen.quit)
    exit_button.grid(row=9, column=0, columnspan=2, pady=5)

    listbox = tk.Listbox(patient_screen, width=100, height=20)
    listbox.grid(row=10, column=0, columnspan=2, pady=5)

    patient_screen.mainloop()


#staff
        
def add_staff():
    name = name_entry.get()
    designation = designation_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()

    if name and designation and address and contact:
        staff_info = {
            "Name": name,
            "Designation": designation,
            "Address": address,
            "Contact": contact
        }
        staff_list.append(staff_info)
        messagebox.showinfo("Success", "Staff added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_staff():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del staff_list[index]
        messagebox.showinfo("Success", "Staff deleted successfully.")
        display_staff()
    else:
        messagebox.showerror("Error", "Please select a staff member to delete.")

def display_staff():
    listbox.delete(0, tk.END)
    for staff in staff_list:
        listbox.insert(tk.END, f"Name: {staff['Name']}, Designation: {staff['Designation']}, Address: {staff['Address']}, Contact: {staff['Contact']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    designation_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

def staff_management():
    global name_entry, designation_entry, address_entry, contact_entry, listbox

    # Creating staff management window
    staff_screen = tk.Tk()
    staff_screen.title("Staff Management")
    staff_screen.geometry("500x400")
    staff_screen.maxsize(500, 400)
    staff_screen.minsize(500, 400)
    staff_screen.configure(bg="#333333")

    # Labels and entry fields for staff details
    tk.Label(staff_screen, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(staff_screen)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(staff_screen, text="Designation:").grid(row=1, column=0, padx=5, pady=5)
    designation_entry = tk.Entry(staff_screen)
    designation_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(staff_screen, text="Address:").grid(row=2, column=0, padx=5, pady=5)
    address_entry = tk.Entry(staff_screen)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(staff_screen, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
    contact_entry = tk.Entry(staff_screen)
    contact_entry.grid(row=3, column=1, padx=5, pady=5)

    # Buttons for staff management operations
    add_button = tk.Button(staff_screen, text="Add Staff", command=add_staff)
    add_button.grid(row=4, column=0, columnspan=2, pady=5)

    delete_button = tk.Button(staff_screen, text="Delete Staff", command=delete_staff)
    delete_button.grid(row=5, column=0, columnspan=2, pady=5)

    display_button = tk.Button(staff_screen, text="Display Staff", command=display_staff)
    display_button.grid(row=6, column=0, columnspan=2, pady=5)

    exit_button = tk.Button(staff_screen, text="Exit", command=staff_screen.destroy)
    exit_button.grid(row=7, column=0, columnspan=2, pady=5)

    # Listbox to display staff details
    listbox = tk.Listbox(staff_screen, width=50)
    listbox.grid(row=8, column=0, columnspan=2, pady=5)

    staff_screen.mainloop()

        
# Function to add a new guest
def add_guest():
    name = name_entry.get()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if name:
        guest_info = {
            "Name": name,
            "Time": time
        }
        guests.append(guest_info)
        messagebox.showinfo("Success", "Guest added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter the guest's name.")

def display_guests():
    listbox.delete(0, tk.END)
    for guest in guests:
        listbox.insert(tk.END, f"Name: {guest['Name']}, Time: {guest['Time']}")

def clear_entries():
    name_entry.delete(0, tk.END)

def guest_time():
    global name_entry, listbox

    guest_screen = tk.Tk()
    guest_screen.title("Guest Management")
    guest_screen.geometry("500x400")
    guest_screen.maxsize(500,400)
    guest_screen.minsize(500,400)
    guest_screen.configure(bg="#333333")

    tk.Label(guest_screen, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(guest_screen)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    add_button = tk.Button(guest_screen, text="Add Guest", command=add_guest)
    add_button.grid(row=1, column=0, columnspan=2, pady=5)

    display_button = tk.Button(guest_screen, text="Display Guests", command=display_guests)
    display_button.grid(row=2, column=0, columnspan=2, pady=5)

    exit_button = tk.Button(guest_screen, text="Exit", command=guest_screen.quit)
    exit_button.grid(row=3, column=0, columnspan=2, pady=5)

    listbox = tk.Listbox(guest_screen, width=50)
    listbox.grid(row=4, column=0, columnspan=2, pady=5)

    guest_screen.mainloop()


# Function to add a new doctor
def add_doctor():
    name = name_entry.get()
    specialization = specialization_entry.get()
    address = address_entry.get()

    if name and specialization and address:
        doctor_info = {
            "Name": name,
            "Specialization": specialization,
            "Address": address
        }
        doctors.append(doctor_info)
        messagebox.showinfo("Success", "Doctor added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def delete_doctor():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del doctors[index]
        messagebox.showinfo("Success", "Doctor deleted successfully.")
        display_doctors()
    else:
        messagebox.showerror("Error", "Please select a doctor to delete.")

def display_doctors():
    listbox.delete(0, tk.END)
    for doctor in doctors:
        listbox.insert(tk.END, f"Name: {doctor['Name']}, Specialization: {doctor['Specialization']}, Address: {doctor['Address']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    specialization_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def doc_time():
    
    global name_entry, specialization_entry, address_entry, listbox
    

    doc_screen = tk.Tk()
    doc_screen.title("Doctor Management")
    doc_screen.geometry("500x400")
    doc_screen.maxsize(500,400)
    doc_screen.minsize(500,400)
    doc_screen.configure(bg="#333333")

   

    tk.Label(doc_screen, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(doc_screen)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(doc_screen, text="Specialization:").grid(row=1, column=0, padx=5, pady=5)
    specialization_entry = tk.Entry(doc_screen)
    specialization_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(doc_screen, text="Address:").grid(row=2, column=0, padx=5, pady=5)
    address_entry = tk.Entry(doc_screen)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    add_button = tk.Button(doc_screen, text="Add Doctor", command=add_doctor)
    add_button.grid(row=3, column=0, columnspan=2, pady=5)

    delete_button = tk.Button(doc_screen, text="Delete Doctor", command=delete_doctor)
    delete_button.grid(row=4, column=0, columnspan=2, pady=5)

    display_button = tk.Button(doc_screen, text="Display Doctors", command=display_doctors)
    display_button.grid(row=5, column=0, columnspan=2, pady=5)

    exit_button = tk.Button(doc_screen, text="Exit", command=doc_screen.quit)
    exit_button.grid(row=6, column=0, columnspan=2, pady=5)

    listbox = tk.Listbox(doc_screen, width=50)
    listbox.grid(row=7, column=0, columnspan=2, pady=5)
    


    doc_screen.mainloop()

def check():
    right_pass = 'pass123'
    our_pass = pass_value.get()
    if right_pass != our_pass:
        tmsg.showinfo("Red Alert", "Incorrect Password")
        capture()
    elif right_pass == our_pass:
        root.destroy()
        next_screen = tk.Tk()
        next_screen.title("Data")
        next_screen.geometry("600x400")
        next_screen.maxsize(600,400)
        next_screen.minsize(600,400)
        image_path = PhotoImage(file=r"C:\Users\Sumesh Saini\Downloads\istockphoto-945589374-612x612.png")
        background_label = tk.Label(next_screen, image=image_path)
        background_label.image = image_path
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        f1 = tk.Frame(next_screen, bg='grey', borderwidth=4)
        f1.pack()
        doc_button = tk.Button(f1, text='Doctor', font=("comicsansms",25,"bold"), relief='groove', pady=10, padx=4, width=10, bg='black', fg='red', command=doc_time)
        patient_button = tk.Button(f1, text='Patient', font=("comicsansms",25,"bold"), relief='groove', pady=10, padx=4, width=10, bg='black', fg='red',command=patient_management)
        staff_button = tk.Button(f1, text='Staff', font=("comicsansms",25,"bold"), relief='groove', pady=10, padx=4, width=10, bg='black', fg='red',command=staff_management)
        guest_button = tk.Button(f1, text='guest', font=("comicsansms",25,"bold"), relief='groove', pady=10, padx=4, width=10, bg='black', fg='red',command=guest_time)
        exit_button = tk.Button(f1, text='Exit', font=("comicsansms",25,"bold"), relief='groove', pady=10, padx=4, command=quit, width=10, bg='black', fg='red')
        doc_button.pack()
        patient_button.pack()
        staff_button.pack()
        guest_button.pack()
        exit_button.pack()
        next_screen.mainloop()

root = tk.Tk()
root.title("Security Check")
root.geometry("500x300")
root.maxsize(500, 300)
root.minsize(500, 300)

image_path = PhotoImage(file=r"C:\Users\Sumesh Saini\Desktop\SECUR.png")
background_label = tk.Label(root, image=image_path)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

login = tk.Label(root, text="LOGIN")
use = tk.Label(root, text="Username", fg='black')
password = tk.Label(root, text="Password")

user_value = tk.StringVar()
pass_value = tk.StringVar()
confirm = tk.IntVar()

use_entry = tk.Entry(root, textvariable=user_value)
pass_entry = tk.Entry(root, textvariable=pass_value, show='*')

submit = tk.Button(root, text="Submit", command=check)
exit_b = tk.Button(root, text="Exit", command=root.quit)
confirm_val = tk.Checkbutton(root, text="I confirm to be a verified employee", variable=confirm)

login.grid(row=0, column=0, columnspan=19, pady=5, padx=5)
use.grid(row=1, column=0)
use_entry.grid(row=1, column=1, pady=7)
password.grid(row=2, column=0)
pass_entry.grid(row=2, column=1)
submit.grid(row=3, column=0, pady=6+3, ipady=3, ipadx=2)
exit_b.grid(row=3, column=1, pady=9, ipady=3, ipadx=2)
confirm_val.grid(row=8, column=1, pady=3, padx=3, ipadx=3, ipady=3)

root.mainloop()

