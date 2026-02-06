#Python program that loops through numbers from 1 to 50 and prints the first number divisible by 7, then stops the loop.

for i in range(1, 51):
    if i % 7 == 0:
        print(i)
        break