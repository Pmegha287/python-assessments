class Father:
    def work(self):
        print("Father works")

class Son(Father):
    pass

s = Son()
s.work()