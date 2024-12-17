from hospital import Hospital, Patient, Doctor
import database
import utils

def main():
    hospital = Hospital()
    database.create_table()

    # Load existing patients from the file when the program starts
    saved_patients = utils.load_patients_from_file()
    for patient_data in saved_patients:
        patient = Patient(
            name=patient_data["name"],
            age=patient_data["age"],
            gender=patient_data["gender"],
            patient_id=patient_data["patient_id"],
            disease=patient_data["disease"])
        hospital.add_patient(patient)

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. View Patients")
        print("4. View Doctors")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter patient name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            disease = input("Enter disease: ")
            patient = Patient(name, age, gender, len(hospital.patients)+1, disease)
            hospital.add_patient(patient)
            database.add_patient_to_db(name, age, gender, disease)
            utils.save_patient_to_file(patient)  # Save to file
            
        elif choice == 2:
            name = input("Enter doctor name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            specialization = input("Enter specialization: ")
            doctor = Doctor(name, age, gender, len(hospital.doctors)+1, specialization)
            hospital.add_doctor(doctor)
        
        elif choice == 3:
            print("Patients in system:")
            patients = database.get_all_patients()
            for patient in patients:
                print(patient)
        
        elif choice == 4:
            print("Doctors in system:")
            hospital.view_doctors()

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
