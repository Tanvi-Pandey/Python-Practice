import numpy as np

print("NUMPY ARRAY CREATION FUNCTIONS\n")

# 1. zeros()
# Creates an array filled with zeros
# Shape: 3 rows × 3 columns

zeros_array = np.zeros((3, 3))

print("1. Zeros Array:")
print(zeros_array)
print()


# 2. ones()
# Creates an array filled with ones
# Shape: 3 rows × 2 columns

ones_array = np.ones((3, 2))

print("2. Ones Array:")
print(ones_array)
print()

# 3. eye()
# Creates an identity matrix
# Diagonal elements are 1
# Rest are 0

identity_matrix = np.eye(3)

print("3. Identity Matrix:")
print(identity_matrix)
print()

# 4. arange()
# Similar to Python range()
# Syntax:
# np.arange(start, stop, step)
# Stop value is NOT included

numbers = np.arange(5, 11, 1)

print("4. Arange Array:")
print(numbers)
print()

# 5. linspace()
# Generates evenly spaced numbers
# Syntax:
# np.linspace(start, stop, number_of_values)
# Stop value IS included

evenly_spaced = np.linspace(0, 100, 6)

print("5. Linspace Array:")
print(evenly_spaced)
print()


# Array Properties

print("ARRAY PROPERTIES \n")

print("Shape of Zeros Array:", zeros_array.shape)
print("Dimensions:", zeros_array.ndim)
print("Total Elements:", zeros_array.size)
print("Data Type:", zeros_array.dtype)
print()

# Real-Life Example
# Student Marks Initialization

student_marks = np.zeros(5)

print("Student Marks Before Entering Scores:")
print(student_marks)

# Suppose marks are entered later
student_marks = np.array([85, 92, 78, 88, 95])

print("\nStudent Marks After Updating:")
print(student_marks)