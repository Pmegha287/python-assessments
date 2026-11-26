class Grandfather:
    def show(self):
        print("Grandfather")

class Father(Grandfather):
    pass

class Son(Father):
    pass

s = Son()
s.show()