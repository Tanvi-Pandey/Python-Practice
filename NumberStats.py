n=int(input("Enter a number: "))

temp = n
count = 0
sum_digits = 0
reverse = 0

while temp > 0:
    digit = temp % 10

    count += 1
    sum_digits += digit

    reverse = reverse * 10 + digit

    temp = temp // 10

print("Digit Count:", count)
print("Sum of Digits:", sum_digits)
print("Reverse:", reverse)