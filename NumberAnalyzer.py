n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")