my_dict = {"name": "Megha", "age": 20}
try:
    print(my_dict["city"])
except KeyError:
    print("Key not found!")