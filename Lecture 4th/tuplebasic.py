# Tuples Basic

myTuple = (78, 90, 75)
studenttuple = ("Ranjeet", "Rahul", "Ravi")

print(myTuple, studenttuple)
print(myTuple)
print(studenttuple)

# Tuples are immutable, so their elements cannot be changed.

# studenttuple[1] = "Dev Verse"    # TypeError: 'tuple' object does not support item assignment

# Empty Tuples

emptyTuple = ()

# Single-element Tuple

singletuple = (1)
singletuple1 = (1,)

print(type(singletuple))     # <class 'int'>
print(type(singletuple1))    # <class 'tuple'>

print(type(emptyTuple))      # <class 'tuple'>
print(type(studenttuple))    # <class 'tuple'>

print(studenttuple.index("Ranjeet"))   # 0
print(studenttuple.count("Manoj"))     # 0
