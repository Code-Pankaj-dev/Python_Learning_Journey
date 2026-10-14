# WAP that prints the sum of first n natural numbers.
# Example: if n = 5, then 1 + 2 + 3 + 4 + 5 = 15
# Hint: Keep a running total inside the loop

n = int(input("Enter the number: "))

total = 0

while n >= 1:
    total = total + n
    n = n - 1

print("Sum =", total)