# Write a function show_age(name, age) that prints:
# "Pankaj Upadhyay is 23 years old."


def show_age(name="Pankaj", age=23):
    print(f"{name} is {age} years old")


show_age("Pankaj Upadhyay", 23)
show_age()
show_age("Dev_Verse", 19)


# Output:
# Pankaj Upadhyay is 23 years old
# Pankaj is 23 years old
# Dev_Verse is 19 years old