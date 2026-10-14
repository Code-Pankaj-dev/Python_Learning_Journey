# Check the Grade Based on Marks

# Constant value: Define the grade based on marks

marks = 90

if marks >= 90:
    print("Your grade is 'A'")
else:
    print("Your grade is 'B'")

# Take marks as input from the user and define the division based on marks

marks = int(input("Enter your marks: "))

if marks >= 60:
    print("You passed 1st Division.")
elif marks >= 45:
    print("You passed 2nd Division.")
elif marks >= 35:
    print("You passed 3rd Division.")
else:
    print("You are Fail.")

# Constant value: Define voting eligibility based on age

age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("End My Code")

# Take age as input from the user and define voting eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
