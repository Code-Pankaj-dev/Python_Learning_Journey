# Practice Question 2

# WAP that takes names of 3 favorite foods from the user

# and stores them in a list. Then print the list and its length.

food1 = input("Enter the first food: ")
food2 = input("Enter the second food: ")
food3 = input("Enter the third food: ")

FoodList = []

FoodList.append(food1)
FoodList.append(food2)
FoodList.append(food3)

print(FoodList)
print("Length of the list:", len(FoodList))
