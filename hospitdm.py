import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Create Patients table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        condition TEXT
    )
''')
conn.commit()

def add_patient(name, age, condition):
    cursor.execute('''
        INSERT INTO Patients (name, age, condition)
        VALUES (?, ?, ?)
    ''', (name, age, condition))
    conn.commit()

def display_patients():
    cursor.execute('''
        SELECT id, name, age, condition
        FROM Patients
    ''')
    patients = cursor.fetchall()

    return patients

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Data Management System")

        # Entry fields
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.condition_var = tk.StringVar()

        # Labels and Entry widgets
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.age_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Condition:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.condition_var).grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Patient", command=self.add_patient).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Display Patients", command=self.display_patients).grid(row=4, column=0, columnspan=2, pady=10)

    def add_patient(self):
        name = self.name_var.get()
        age = self.age_var.get()
        condition = self.condition_var.get()

        if name and age and condition:
            try:
                age = int(age)
                add_patient(name, age, condition)
                messagebox.showinfo("Success", "Patient added successfully.")
            except ValueError:
                messagebox.showerror("Error", "Invalid age. Please enter a valid number.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_patients(self):
        patients = display_patients()

        if patients:
            result_window = tk.Toplevel(self.root)
            result_window.title("Patient List")

            tk.Label(result_window, text="ID").grid(row=0, column=0)
            tk.Label(result_window, text="Name").grid(row=0, column=1)
            tk.Label(result_window, text="Age").grid(row=0, column=2)
            tk.Label(result_window, text="Condition").grid(row=0, column=3)

            for i, patient in enumerate(patients, start=1):
                tk.Label(result_window, text=patient[0]).grid(row=i, column=0)
                tk.Label(result_window, text=patient[1]).grid(row=i, column=1)
                tk.Label(result_window, text=patient[2]).grid(row=i, column=2)
                tk.Label(result_window, text=patient[3]).grid(row=i, column=3)
        else:
            messagebox.showinfo("Info", "No patients to display.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
print("Thanks")