# Methods in list 
# List are mutable
marks = [80, 50, 65, 75, 85, 95, 91, 88, 97]
print(marks)

marks[2] = 77
print(marks)


# Slicing 
print(marks[:5])   # [80, 50, 65, 75, 85]

print(max(marks))  # 97
print(min(marks))   # 50
marks.append(70)    # Add  70 in last 
print(marks)
marks.sort()
print(marks)
marks.pop(2)
print(marks)
marks.remove(97)
print(marks)
marks.insert(2, 101)
print(marks)



#String are immutable
name = "Saumya"
name[1] = "o"          #TypeError: 'str' object does not support item assignment
print(name)
