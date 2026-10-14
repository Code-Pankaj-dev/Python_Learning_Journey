# Create a function add_numbers(a, b)
# that prints sum, difference, multiplication and division.


def add_numbers(a=10, b=17):
    total = a + b
    diff = a - b
    multi = a * b
    div = a / b

    print(f"Sum of {a} and {b}:", total)
    print(f"Difference of {a} and {b}:", diff)
    print(f"Multiplication of {a} and {b}:", multi)
    print(f"Division of {a} and {b}:", div)


add_numbers(100, 200)
add_numbers()
add_numbers(1000, 300)