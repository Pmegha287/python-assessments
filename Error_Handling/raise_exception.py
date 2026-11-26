age = int(input("Enter age: "))
try:
    if age < 18:
        raise ValueError("Age must be 18+")
    print("You can vote!")
except ValueError as e:
    print(e)