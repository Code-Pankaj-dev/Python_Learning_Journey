    # Convert text-based emotions into Emojis.
    # Code Examples:
    #  Emoji Converter - Basic Version (No if, no loop)

msg = input("Enter your message: ")
msg = msg.replace(":)","😊")
msg = msg.replace(":(","😉")
msg = msg.replace(":D","🥰")
msg = msg.replace(":;","😂")

print(msg)
