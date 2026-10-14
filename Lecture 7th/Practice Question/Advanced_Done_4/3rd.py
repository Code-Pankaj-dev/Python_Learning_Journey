# Create a recursive function for countdown.

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


# Direct value
countdown(5)


# Input method
number = int(input("Enter a number to start countdown: "))
countdown(number)
