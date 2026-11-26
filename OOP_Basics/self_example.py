class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("My name is", self.name)

s = Student("Megha")
s.show()