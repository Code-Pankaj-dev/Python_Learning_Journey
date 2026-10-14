# Create a function using `*args`.
#   1. Simple *args example

def display_args(*args):
    print(args)

display_args(10, 20, 30, 40, 50, 60)

#  2. Practical *args example


def total(*args):
    result = 0

    for num in args:
        result += num

    return result


print(total(10, 20, 30))
print(total(5, 10, 15, 20))
