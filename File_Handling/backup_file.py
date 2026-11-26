with open("sample.txt", "r") as src, open("backup.txt", "w") as dest:
    dest.write(src.read())
print("Backup created")