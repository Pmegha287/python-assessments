class Student:
    def __init__(self, name):
        self.name = name

s = Student("Megha")
print(s.name)
s.name = "Priya"
print(s.name)