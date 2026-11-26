try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Program Finished")