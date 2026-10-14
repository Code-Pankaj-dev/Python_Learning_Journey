#  Email Domain 
email = input("Enter the Email I'D: ").strip().lower()

if email.endswith("@gmail.com"):
    print("Gmail Account")
else:
    print("Invalid Email")

print(email)