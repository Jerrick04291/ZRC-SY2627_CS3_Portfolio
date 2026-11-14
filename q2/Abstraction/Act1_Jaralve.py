class Patient:
    def __init__(self, name, bill):
        self.name = name
        self.bill = bill

    def calculate_bill(self):
        return self.bill

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill * 0.8

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.bill * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Maria Santos", 15000)
patient3 = PhilhealthPatient("Pedro Reyes", 15000)

patients = [patient1, patient2, patient3]

for patient in patients:
    print("Patient Name:", patient.name)
    patient.display_patient_type()
    print("Total Bill: ₱", patient.calculate_bill())