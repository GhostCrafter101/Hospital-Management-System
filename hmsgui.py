import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from ttkthemes import ThemedTk
import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establishes and returns a new database connection."""
    return mysql.connector.connect(host="sql12.freemysqlhosting.net",
                                   user="sql12731202",
                                   password="jHmCD3Vye7",
                                   database="sql12731202")

# Function to Add Patient
def add_patient(name, age, gender, contact, address):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO patients (patient_name, patient_age, patient_gender, patient_contact, patient_address) VALUES (%s, %s, %s, %s, %s)"
            values = (name, age, gender, contact, address)
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Patient added successfully.")
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to Add Doctor
def add_doctor(name, specialization, contact, available_days):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO doctors (doctor_name, specialization, contact_number, available_days) VALUES (%s, %s, %s, %s)"
            values = (name, specialization, contact, available_days)
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Doctor added successfully.")
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to Schedule Appointment
def schedule_appointment(patient_id, doctor_id, date, time):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status) VALUES (%s, %s, %s, %s, 'Scheduled')"
            values = (patient_id, doctor_id, date, time)
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Appointment scheduled successfully.")
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to Generate Bill
def generate_bill(patient_id, treatment_cost, doctor_fee):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO billing (patient_id, treatment_cost, doctor_fee, date_of_billing) VALUES (%s, %s, %s, CURDATE())"
            values = (patient_id, treatment_cost, doctor_fee)
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Bill generated successfully.")
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to View Records (generic)
def view_records(query):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []

# Function to Display Records in a Listbox
def display_records(listbox, query):
    records = view_records(query)
    listbox.delete(0, tk.END)
    for record in records:
        listbox.insert(tk.END, record)

# GUI Application
def create_gui():
    root = ThemedTk(theme="radiance")  # Updated theme for better aesthetics
    root.title("Hospital Management System")
    root.geometry("800x600")  # Increased window size for better layout
    root.configure(bg="#f0f0f0")  # Light gray background color

    tab_control = ttk.Notebook(root)

    # Add Patient Tab
    tab_add_patient = ttk.Frame(tab_control)
    tab_control.add(tab_add_patient, text="Add Patient")
    ttk.Label(tab_add_patient, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_entry = ttk.Entry(tab_add_patient)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(tab_add_patient, text="Age").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    age_entry = ttk.Entry(tab_add_patient)
    age_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Label(tab_add_patient, text="Gender").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    gender_entry = ttk.Entry(tab_add_patient)
    gender_entry.grid(row=2, column=1, padx=10, pady=5)
    ttk.Label(tab_add_patient, text="Contact").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    contact_entry = ttk.Entry(tab_add_patient)
    contact_entry.grid(row=3, column=1, padx=10, pady=5)
    ttk.Label(tab_add_patient, text="Address").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    address_entry = ttk.Entry(tab_add_patient)
    address_entry.grid(row=4, column=1, padx=10, pady=5)

    def submit_patient():
        add_patient(name_entry.get(), age_entry.get(), gender_entry.get(), contact_entry.get(), address_entry.get())

    ttk.Button(tab_add_patient, text="Add Patient", command=submit_patient).grid(row=5, column=0, columnspan=2, pady=10)

    # Add Doctor Tab
    tab_add_doctor = ttk.Frame(tab_control)
    tab_control.add(tab_add_doctor, text="Add Doctor")
    ttk.Label(tab_add_doctor, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    doc_name_entry = ttk.Entry(tab_add_doctor)
    doc_name_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(tab_add_doctor, text="Specialization").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    specialization_entry = ttk.Entry(tab_add_doctor)
    specialization_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Label(tab_add_doctor, text="Contact").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    doc_contact_entry = ttk.Entry(tab_add_doctor)
    doc_contact_entry.grid(row=2, column=1, padx=10, pady=5)
    ttk.Label(tab_add_doctor, text="Available Days").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    available_days_entry = ttk.Entry(tab_add_doctor)
    available_days_entry.grid(row=3, column=1, padx=10, pady=5)

    def submit_doctor():
        add_doctor(doc_name_entry.get(), specialization_entry.get(), doc_contact_entry.get(), available_days_entry.get())

    ttk.Button(tab_add_doctor, text="Add Doctor", command=submit_doctor).grid(row=4, column=0, columnspan=2, pady=10)

    # Schedule Appointment Tab
    tab_schedule_appointment = ttk.Frame(tab_control)
    tab_control.add(tab_schedule_appointment, text="Schedule Appointment")
    ttk.Label(tab_schedule_appointment, text="Patient ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    patient_id_entry = ttk.Entry(tab_schedule_appointment)
    patient_id_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(tab_schedule_appointment, text="Doctor ID").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    doctor_id_entry = ttk.Entry(tab_schedule_appointment)
    doctor_id_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Label(tab_schedule_appointment, text="Date").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    date_entry = DateEntry(tab_schedule_appointment, date_pattern='yyyy-mm-dd')
    date_entry.grid(row=2, column=1, padx=10, pady=5)
    ttk.Label(tab_schedule_appointment, text="Time").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    time_entry = ttk.Spinbox(tab_schedule_appointment, values=[f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 30)], width=8)
    time_entry.grid(row=3, column=1, padx=10, pady=5)

    def submit_appointment():
        schedule_appointment(patient_id_entry.get(), doctor_id_entry.get(), date_entry.get(), time_entry.get())

    ttk.Button(tab_schedule_appointment, text="Schedule Appointment", command=submit_appointment).grid(row=4, column=0, columnspan=2, pady=10)

    # View Patients Tab
    tab_view_patients = ttk.Frame(tab_control)
    tab_control.add(tab_view_patients, text="View Patients")
    listbox_patients = tk.Listbox(tab_view_patients, width=70, height=20, bg="#ffffff", fg="#000000", font=("Arial", 10))
    listbox_patients.grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(tab_view_patients, text="Refresh", command=lambda: display_records(listbox_patients, "SELECT * FROM patients")).grid(row=1, column=0, pady=10)

    # View Doctors Tab
    tab_view_doctors = ttk.Frame(tab_control)
    tab_control.add(tab_view_doctors, text="View Doctors")
    listbox_doctors = tk.Listbox(tab_view_doctors, width=70, height=20, bg="#ffffff", fg="#000000", font=("Arial", 10))
    listbox_doctors.grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(tab_view_doctors, text="Refresh", command=lambda: display_records(listbox_doctors, "SELECT * FROM doctors")).grid(row=1, column=0, pady=10)

    # View Appointments Tab
    tab_view_appointments = ttk.Frame(tab_control)
    tab_control.add(tab_view_appointments, text="View Appointments")
    listbox_appointments = tk.Listbox(tab_view_appointments, width=70, height=20, bg="#ffffff", fg="#000000", font=("Arial", 10))
    listbox_appointments.grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(tab_view_appointments, text="Refresh", command=lambda: display_records(listbox_appointments, "SELECT * FROM appointments")).grid(row=1, column=0, pady=10)

    # Generate Bill Tab
    tab_generate_bill = ttk.Frame(tab_control)
    tab_control.add(tab_generate_bill, text="Generate Bill")
    ttk.Label(tab_generate_bill, text="Patient ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    bill_patient_id_entry = ttk.Entry(tab_generate_bill)
    bill_patient_id_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(tab_generate_bill, text="Treatment Cost").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    treatment_cost_entry = ttk.Entry(tab_generate_bill)
    treatment_cost_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Label(tab_generate_bill, text="Doctor Fee").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    doctor_fee_entry = ttk.Entry(tab_generate_bill)
    doctor_fee_entry.grid(row=2, column=1, padx=10, pady=5)

    def submit_bill():
        generate_bill(bill_patient_id_entry.get(), treatment_cost_entry.get(), doctor_fee_entry.get())

    ttk.Button(tab_generate_bill, text="Generate Bill", command=submit_bill).grid(row=3, column=0, columnspan=2, pady=10)

    # View Bills Tab
    tab_view_bills = ttk.Frame(tab_control)
    tab_control.add(tab_view_bills, text="View Bills")
    listbox_bills = tk.Listbox(tab_view_bills, width=70, height=20, bg="#ffffff", fg="#000000", font=("Arial", 10))
    listbox_bills.grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(tab_view_bills, text="Refresh", command=lambda: display_records(listbox_bills, "SELECT * FROM billing")).grid(row=1, column=0, pady=10)

    tab_control.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    create_gui()

