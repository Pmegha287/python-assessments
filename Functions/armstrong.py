def is_armstrong(n):
    s = str(n)
    total = sum(int(d) ** len(s) for d in s)
    return total == n

print(is_armstrong(153))
print(is_armstrong(123))