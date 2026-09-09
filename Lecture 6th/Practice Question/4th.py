# WAP that print the sum of first m natural numbers. 
# For Examples: if num = 5, then output shoud be 1+2+3+4+5=15
# (Hint: keep a running total inside the loop)
 
n = int(input("Enter the number: "))

sum= 0
while n>=1:
    sum = sum+n
    n=n-1

    print("Sum=",sum)
    print("n=",n)
 