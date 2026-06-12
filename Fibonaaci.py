n = int(input("How many terms? "))

a = 0  #current and next fib num
b = 1

for i in range(n): #loop till bedore n
    print(a, end=" ") #pprevents newline 
    a, b = b, a + b  #both a and b simultaneously assigned