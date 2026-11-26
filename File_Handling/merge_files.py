with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
    out.write(f1.read() + "\n" + f2.read())
print("Merged successfully")