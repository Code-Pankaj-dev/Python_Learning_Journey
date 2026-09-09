# Dictionary Basic

College={
   "name" : "MMIT Kushnagar", 
   "city" : "Kushinagar",
   "age"  : 19,
   "rollnumber" : 31,
   "name" : "Dev_Verse"
}

# College["aadhar"] = "878754329345"   # Add another Key and Keys value
# print(College)
# College["city"] = "SiddharthNagar"
# print(College)

# College.pop("aadhar")
# print(College)

# print(type(College))  # print college dictonary data type
# print(College["name"]) # print college name 
# print(College)  #  print all key of college
# print(College["age"])   # prnt age
# print(College["city"]) #print city

# print(College["rollnumber"])  # print rollnumber


print(College.keys())   #print only Keys/ print All Keys
##Output: dict_keys(['name', 'city', 'age', 'rollnumber'])
print(College.items())     
#Output:  dict_items([('name', 'Dev_Verse'), ('city', 'Kushinagar'), ('age', 19), ('rollnumber', 31)])
print(College.popitem())
# print(College.setdefault()) 