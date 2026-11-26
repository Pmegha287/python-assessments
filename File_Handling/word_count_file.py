with open("sample.txt", "r") as f:
    text = f.read().lower().split()
    freq = {}
    for w in text:
        freq[w] = freq.get(w, 0) + 1
    print(freq)