"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryType, commissionType):
        self.name = name
        self.salaryType = salaryType
        self.commissionType = commissionType
        self.salaryContract = 0
        self.hourlyContract = 0
        self.bonusCommission = 0
        self.contractCommission = 0
        self.hoursWorked = 0
        self.numOfContracts = 0

    def get_pay(self):

        basePay = 0
        commissionPay = 0
        pay = 0

        if (self.salaryType == "monthly"):
            basePay = self.salaryContract

        if (self.salaryType == "hourly"):
            basePay = self.hoursWorked * self.hourlyContract

        if (self.commissionType == "contract"):
            commissionPay = self.numOfContracts * self.contractCommission

        if (self.commissionType == "bonus"):
            commissionPay = self.bonusCommission

        pay = basePay + commissionPay
        return pay


    def __str__(self):

        string = ""


        if (self.salaryType == "monthly"):
            string = (f'{self.name} works on a monthly salary of {self.salaryContract}')
        if (self.salaryType == "hourly"):
            string = (f'{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyContract}/hour')
        if (self.commissionType == "contract"):
            string = string + (f' and receives a commission for {self.numOfContracts} contract(s) at {self.contractCommission}/contract')
        if (self.commissionType == "bonus"):
            string = string + (f' and receives a bonus commission of {self.bonusCommission}')

        string = string + (f'. Their total pay is {self.get_pay()}.')
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", "none")
billie.salaryContract = 4000


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", "none")
charlie.hourlyContract = 25
charlie.hoursWorked= 100

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", "contract")
renee.salaryContract = 3000
renee.contractCommission = 200
renee.numOfContracts = 4

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", "contract")
jan.hourlyContract = 25
jan.hoursWorked = 150
jan.contractCommission = 220
jan.numOfContracts = 3

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", "bonus")
robbie.salaryContract = 2000
robbie.bonusCommission = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", "bonus")
ariel.hourlyContract = 30
ariel.hoursWorked = 120
ariel.bonusCommission = 600
