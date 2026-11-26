word = input("Enter word: ")
count = 0
for ch in word:
    if ch == "a":
        count = count + 1
print("Count of a:", count)