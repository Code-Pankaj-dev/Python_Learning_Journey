#Practice Question2:
#WAP that takes your favorite food name as input and print:
#1. The Middle 3 characters
#2. The last 2 characters

Food = input("Enter Your Favorite Food: ")
mid = len(Food)//2
result = Food[mid-1:mid+1]
print("Your Favorite Food is: ", Food)
print(result)
