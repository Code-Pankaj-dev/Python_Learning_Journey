#  MINI PROJECT-Count-down Timer(with 1-second gap)
#  Goal: Print a countdown before something "exciting" happens (like "Launching..." or "Happy New Year")
# concept Use: for loop, range(), and the time module.


import time
count =  int(input("Enter the Count-Down Number: "))
print("===Count-Down Start Now===")
for i in range(count, 0, -1):
    print(i)
    time.sleep(2)
print("Happy New Year......!")