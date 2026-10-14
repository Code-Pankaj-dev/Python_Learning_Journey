# WAP to print this pattern using a while loop
# *
# * *
# * * *
# * * * *

num = 1

while num <= 4:
    print("* " * num)
    num = num + 1



# Take value from user, then print the pattern

star = int(input("Enter the value: "))

num = 1

while num <= star:
    print("* " * num)
    num = num + 1