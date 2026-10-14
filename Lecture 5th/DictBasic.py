# Dictionary Basic

College = {
    "name": "Dev_Verse",
    "city": "Kushinagar",
    "age": 19,
    "rollnumber": 31
}

# Print all keys
print(College.keys())

# Print all key-value pairs
print(College.items())

# Remove and return the last inserted item
print(College.popitem())

# Add a key with a default value if it does not exist
# print(College.setdefault("country", "India"))



# Add a new key and value
# College["aadhar"] = "XXXXXXXXXXXX"
# print(College)

# Update an existing value
# College["city"] = "SiddharthNagar"
# print(College)

# Remove a key
# College.pop("aadhar")
# print(College)

# Print dictionary data type
# print(type(College))

# Access a value using its key
# print(College["name"])
# print(College["age"])
# print(College["city"])
# print(College["rollnumber"])