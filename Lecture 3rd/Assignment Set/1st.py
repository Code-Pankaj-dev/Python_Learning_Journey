#  1. WAP that takes a sentence and prints:
#       * Total characters (len())
#      * Uppercase Version
#      * Lowercase Version


Sen = input("Enter the Any Sentence: ")
print()
print("Total Characters of This Sentence:", len(Sen))
print(Sen.upper())    #      * Uppercase Version
print(Sen.lower())    #      * Lowercase Version
print(Sen.title())
print(Sen.count("A"))
print(Sen.find("a"))
print(Sen.encode())