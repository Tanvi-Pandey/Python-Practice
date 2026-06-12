s = int(input("Start: "))
e = int(input("End: "))

for n in range(s, e + 1):
    if n > 1:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)