n = int(input("Enter a number: "))

isPrime=True

if n<= 1:
    isPrime=False
else:
    for i in range(2, n):
        if n%i==0:
            isPrime=False
            break

if isPrime:
    print("Prime Number")
else:
    print("Not Prime Number")