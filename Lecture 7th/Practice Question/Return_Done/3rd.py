# Write a function that takes a string
# and returns the count of vowels and consonants separately.


def countVowConso(userInput):
    vowels = "aeiouAEIOU"

    countVowel = 0
    countConsonant = 0

    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowel += 1
            else:
                countConsonant += 1

    return countVowel, countConsonant


vowels, consonants = countVowConso("Pankaj Upadhyay")

print("Vowels =", vowels)
print("Consonants =", consonants)