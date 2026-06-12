n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
o = input("Enter operator (+, -, *, /): ")

if o == "+":
    print("Result:", n1 + n2)

elif o == "-":
    print("Result:", n1 - n2)

elif o == "*":
    print("Result:", n1 * n2)

elif o == "/":
    if n2 != 0:
        print("Result:", n1 / n2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")