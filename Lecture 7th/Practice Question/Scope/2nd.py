# Use the `global` keyword to modify a global variable.
def modify_global():
    global x  # Declare x as a global variable
    x += 5    # Modify the global variable
x = 10  # Initialize the global variable
modify_global()
print("Modified global variable:", x)
