class Programmer:
    Company="Microsoft"
    def __init__(self, Name, Salary, Zipcode):
        self.Name=Name
        self.Salary=Salary
        self.Zipcode=Zipcode

info=Programmer("Ali", 120000, 1234900)
print(info.Name, info.Salary, info.Zipcode, info.Company)

y=Programmer("Ahmed", 120000, 1234900)
print(y.Name, y.Salary, y.Zipcode, y.Company)