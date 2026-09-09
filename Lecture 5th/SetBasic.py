teacher = { "Arvind Kushwaha", "Vinod Guru G", " Manoj Sir", "Rahman Sir", "Madhu Ma'am", "Vivekanand Sir"}
print(type(teacher))  
print(teacher)
teacher = { "Arvind Kushwaha", "Vinod Guru G", "Manoj Sir", "Rahman Sir", "Madhu Ma'am", "Vivekanand Sir", "Manoj Sir"}
#output: <class 'set'>
print(teacher)
# #Output: {'Arvind Kushwaha', 'Vivekanand Sir', ' Manoj Sir', 'Rahman Sir', 'Vinod Guru G', "Madhu Ma'am"}
teacher.add("Nilesh Sir")
print(teacher)
teacher.remove("Manoj Sir")
print(teacher)   
teacher.clear()
print(teacher)
# print(tuple())
# #Output: ()


# # Create empty set:

# emptySet = set()
# print(type(emptySet))