with open("sentences.txt", "w") as f:
    for i in range(5):
        s = input(f"Enter sentence {i+1}: ")
        f.write(s + "\n")
print("Written successfully")