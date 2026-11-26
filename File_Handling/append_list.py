s1 = input("Enter sentence 1: ")
s2 = input("Enter sentence 2: ")

with open("sample.txt", "a") as f:
    f.write("\n" + s1 + "\n" + s2)

print("Added successfully!")