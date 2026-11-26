class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

calc = Calculator()
print("Add:", calc.add(10, 5))
print("Sub:", calc.sub(10, 5))