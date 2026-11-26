class Bird:
    def fly(self):
        print("Bird flies")

class Aeroplane:
    def fly(self):
        print("Aeroplane flies")

for obj in [Bird(), Aeroplane()]:
    obj.fly()