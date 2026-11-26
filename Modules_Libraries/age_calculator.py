import datetime

birth_year = int(input("Enter birth year: "))
current_year = datetime.date.today().year
print("Your age:", current_year - birth_year)