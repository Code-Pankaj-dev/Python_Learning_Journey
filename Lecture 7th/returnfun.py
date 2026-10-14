# ==========================================
#           RETURN STATEMENT
# ==========================================


# Function Definition
def multiply(a=10, b=20):
    return a * b


# Function Calling with Arguments
print("Multiplication =", multiply(40, 45))


# Return value ko variable me store karna
result = multiply(5, 15)
print("Result =", result)


# Default Arguments
# Agar koi argument nahi diya gaya,
# to a = 10 aur b = 20 use hoga.

result = multiply()
print("Default Result =", result)