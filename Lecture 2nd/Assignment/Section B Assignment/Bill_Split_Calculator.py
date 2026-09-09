#Question(2nd): Write a Program that takes total bill amount and number of friends as input     Calculate how much each person will pay. 
#Also print the data type of each variable used.
#  (HINT: use float() and division Operator)

bill = float(input("Enter the total Bill Amout: "))
friends = int(input("Numbar of Friends: "))

equal_amount = bill/friends

print("Avery Persion Payable Amount", equal_amount)

print("Data Type of Total Bill Amount: ", type(bill))
print("Data Type of Number of Friends: ", type(friends))    
print("Data Type of Each Person Payable Amount: ", type(equal_amount))