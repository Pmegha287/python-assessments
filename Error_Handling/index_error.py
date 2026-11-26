my_list = [10, 20, 30]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range!")