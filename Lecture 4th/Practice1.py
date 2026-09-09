#WAP that takes a number as input and prints:
#   * "Positive" if number > 0
#   * "Zero" if number == 0
#   * "Negative" if number < 0


store = int(input("Enter the Value: "))
if(store >= 1):
    print("Positive Value")
elif(store <= -1):
    print("Negative Value")
else:
    print("Zero")