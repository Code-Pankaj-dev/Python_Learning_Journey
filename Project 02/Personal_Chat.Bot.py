# Rule-Based AI Python ChatBot

import datetime

# Take user's name
name = input("Enter your name: ")

# Get current hour
presentHour = datetime.datetime.now().hour

# Greeting according to time
if 5 <= presentHour < 12:
    print("Good Morning,", name)
elif 12 <= presentHour < 17:
    print("Good Afternoon,", name)
elif 17 <= presentHour < 21:
    print("Good Evening,", name)
else:
    print("Good Night,", name)


print("\nHi! Welcome to this ChatBot.")
print("You can ask basic questions.")
print("Type 'bye' to exit from the bot.")


# ChatBot Memory - Dictionary of Responses

responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I am fine. Thank you!",
    "who are you": "I am Dev ChatBot.",
    "motivate me": "Failure is not the opposite of success. It is part of success."
}


# Function to get response from ChatBot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to answer this question. I am still in learning mode."


# Take user input

while True:

    userInput = input("\nPlease ask a question: ")

    # Exit condition
    if "bye" in userInput.lower():
        print("Bot Response: Goodbye! Have a great day!")
        break

    reply = getResponseOfBot(userInput)

    print("Bot Response:", reply)