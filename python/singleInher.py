class College:
    Cname = "ACET"  # Fixed: Made it a class variable so other classes can access it

class Student(College):
    def __init__(self, name):  # Fixed: Added the __init__ constructor method
        self.name = name
        
    def name_S(self):  # Fixed: Added 'self' parameter to reference the instance
        print(f'{self.name} is studying in {College.Cname}')

s = Student("Satya")
s.name_S()