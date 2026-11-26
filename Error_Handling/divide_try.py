try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")