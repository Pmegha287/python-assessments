try:
    password = input("Enter password: ")
    if password != "1234":
        raise Exception("Wrong password!")
    print("Login Successful!")
except Exception as e:
    print(e)