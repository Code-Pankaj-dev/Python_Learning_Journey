# Call a function using keyword arguments.
def student_info(name, age, grade):
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)

# Calling the function using keyword arguments
student_info(name="Alice", age=20, grade="A")
student_info(grade="B", name="Bob", age=22)  # Order doesn't matter with keyword arguments
student_info(age=19, name="Charlie", grade="C")
student_info("David", grade="D", age=21)  # Mixing positional and keyword arguments
student_info("Eve", age=23, grade="B")  # Positional argument followed by keyword arguments