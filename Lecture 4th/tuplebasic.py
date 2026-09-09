# Tuples Basic

myTuple = (78,90,75)
studenttuple = ("Ranjeet", "Rahul", "Ravi")
print(myTuple, studenttuple)
print(myTuple)
print(studenttuple)

# studenttuple[1] = "Dev Verse"      # tuples are not changeable


# Empty Tuples
emptyTuple = ()
singletuple = (1)    
singletuple1 = (1,) 

print(type(singletuple))    # <class 'int'>
print(type(singletuple1))   # <class 'tuple'>

print(type(emptyTuple))
print(type(studenttuple))
print(studenttuple.index("Ranjeet"))
print(studenttuple.count("Manoj"))