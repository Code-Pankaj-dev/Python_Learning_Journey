# MINI PROJECT - Countdown Timer (with 1-second gap)
# Goal: Print a countdown before something exciting happens
# Concept Used: for loop, range(), and the time module

import time

count = int(input("Enter the Countdown Number: "))

print("=== Countdown Start Now ===")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("🚀 Countdown Complete! Let's Begin!")

# OUTPUT:
# Enter the Countdown Number: 5
# === Countdown Start Now ===
# 5
# 4
# 3
# 2
# 1
# Happy New Year......!