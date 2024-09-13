import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establishes and returns a new database connection."""
    return mysql.connector.connect(host="sql12.freemysqlhosting.net",
                                   user="sql12731202",
                                   password="jHmCD3Vye7",
                                   database="sql12731202")


def add_patient(name, age, gender, contact, address):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO patients (patient_name, patient_age, patient_gender, patient_contact, patient_address) VALUES (%s, %s, %s, %s, %s)"
            values = (name, age, gender, contact, address)
            cursor.execute(query, values)
            db_connection.commit()
            print("Patient added successfully.")
    except Error as err:
        print(f"Error: {err}")


def add_doctor(name, specialization, contact, available_days):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO doctors (doctor_name, specialization, contact_number, available_days) VALUES (%s, %s, %s, %s)"
            values = (name, specialization, contact, available_days)
            cursor.execute(query, values)
            db_connection.commit()
            print("Doctor added successfully.")
    except Error as err:
        print(f"Error: {err}")


def view_patients():
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "SELECT * FROM patients"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)    

    except Error as err:
        print(f"Error: {err}")


def schedule_appointment(patient_id, doctor_id, date, time):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status) VALUES (%s, %s, %s, %s, 'Scheduled')"
            values = (patient_id, doctor_id, date, time)
            cursor.execute(query, values)
            db_connection.commit()
            print("Appointment scheduled successfully.")
    except Error as err:
        print(f"Error: {err}")


def generate_bill(patient_id, treatment_cost, doctor_fee):
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "INSERT INTO billing (patient_id, treatment_cost, doctor_fee, date_of_billing) VALUES (%s, %s, %s, CURDATE())"
            values = (patient_id, treatment_cost, doctor_fee)
            cursor.execute(query, values)
            db_connection.commit()
            print("Bill generated successfully.")
    except Error as err:
        print(f"Error: {err}")

def view_doctors():
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "SELECT * FROM doctors"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)    
                
    except Error as err:
        print(f"Error: {err}")        

def view_appointments():
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "SELECT * FROM appointments"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)    
                
    except Error as err:
        print(f"Error: {err}")

def view_bills():
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor()
            query = "SELECT * FROM billing"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)    
                
    except Error as err:
        print(f"Error: {err}")        

def main_menu():
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Schedule Appointment")
        print("6. View Appointments")
        print("7. Generate Bill")
        print("8. View bills")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            contact = input("Enter patient contact: ")
            address = input("Enter patient address: ")
            add_patient(name, age, gender, contact, address)

        elif choice == '2':
            view_patients()

        elif choice == '3':
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            contact = input("Enter doctor contact number: ")
            available_days = input("Enter available days: ")
            add_doctor(name, specialization, contact, available_days)

        elif choice == '4':
            view_doctors()    

        elif choice == '5':
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            schedule_appointment(patient_id, doctor_id, date, time)

        elif choice == '6':
            view_appointments()    

        elif choice == '7':
            patient_id = int(input("Enter patient ID: "))
            treatment_cost = float(input("Enter treatment cost: "))
            doctor_fee = float(input("Enter doctor fee: "))
            generate_bill(patient_id, treatment_cost, doctor_fee)

        elif choice == '8':
            view_bills()    

        elif choice == '9':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu() 

# made by ghostcrafter101 -