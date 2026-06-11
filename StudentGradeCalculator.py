m1=float(input("Enter marks for subject 1:"))
m2=float(input("Enter marks for subject 2:"))
m3=float(input("Enter marks for subject 3:"))
m4=float(input("Enter marks for subject 4:"))
m5=float(input("Enter marks for subject 5:"))

t=m1+m2+m3+m4+m5

p=t/5

print("Percentage:",p)

if p>=90:
    print("Grade: A")
elif p>=75:
    print("Grade: B")
elif p>=60:
    print("Grade: C")
elif p>=40:
    print("Grade: D")
else:
    print("Grade: F")
