# Parent class
class Patient:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return 0.0

    def set_bill_amount(self, amount):
        self.bill_amount = amount

    def calculate_bill(self):
        return self.bill_amount
    
class SeniorPatient(Patient):
    def get_bill_amount(self):
        return self.bill_amount
    
    def calculate_bill(self):
        return self.bill_amount * 0.8  
    
class PhilHealthPatient(Patient):
    def get_bill_amount(self):
        return self.bill_amount
    
    def calculate_bill(self):
        return self.bill_amount * 0.85

patient1 = Patient("Generic Patient")
senior1 = SeniorPatient("John Doe")
philhealth1 = PhilHealthPatient("Jane Smith")

patient1.set_bill_amount(15000)
senior1.set_bill_amount(15000)
philhealth1.set_bill_amount(15000)

print("Generic Patient Bill:", patient1.calculate_bill())
print("Senior Patient Bill:", senior1.calculate_bill())
print("PhilHealth Patient Bill:", philhealth1.calculate_bill())
