import random

dice = random.randint(1, 6)
print("Dice rolled:", dice)
if dice == 6:
    print("You Win!")
else:
    print("Try Again!")