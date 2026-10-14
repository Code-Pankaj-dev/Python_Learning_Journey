# Set Basic
teacher = {
    "Arvind Kushwaha",
    "Vinod Guru G",
    "Manoj Sir",
    "Rahman Sir",
    "Madhu Ma'am",
    "Vivekanand Sir"
}
print(type(teacher))
print(teacher)

# Duplicate elements are automatically removed
teacher = {
    "Arvind Kushwaha",
    "Vinod Guru G",
    "Manoj Sir",
    "Rahman Sir",
    "Madhu Ma'am",
    "Vivekanand Sir",
    "Manoj Sir"
}
print(teacher)

# Add a new element
teacher.add("Nilesh Sir")
print(teacher)

# Remove an element
teacher.remove("Manoj Sir")
print(teacher)

# Remove all elements
teacher.clear()
print(teacher)

# Create an empty set

emptySet = set()
print(type(emptySet))
print(emptySet)