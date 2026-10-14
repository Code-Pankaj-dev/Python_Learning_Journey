# Methods in List
# Lists are mutable

marks = [80, 50, 65, 75, 85, 95, 91, 88, 97]
print(marks)

# Modifying a List
marks[2] = 77
print(marks)

# Slicing
print(marks[:5])   # [80, 50, 77, 75, 85]

# max() and min()
print(max(marks))  # 97
print(min(marks))  # 50

# append() - Adds an element at the end
marks.append(70)
print(marks)

# sort() - Sorts the list in ascending order
marks.sort()
print(marks)

# pop() - Removes an element using its index
marks.pop(2)
print(marks)

# remove() - Removes the first occurrence of a value
marks.remove(97)
print(marks)

# insert() - Inserts an element at a specific index
marks.insert(2, 101)
print(marks)

# Strings are immutable
name = "Saumya"

# This will cause a TypeError because strings cannot be changed
name[1] = "o"   # TypeError: 'str' object does not support item assignment
print(name)
