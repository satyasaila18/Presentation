class College:
    Cname = "ACET" 

class Student(College):
    def __init__(self, name):  
        self.name = name
        
    def name_S(self):  
        print(f'{self.name} is studying in {College.Cname}')

s = Student("Satya")
s.name_S()

p=Student("Virat")
p.name_S()