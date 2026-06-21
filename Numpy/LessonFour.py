import numpy as np

# Create the array
scores = np.array([45, 67, 89, 32, 76])

print("Original Scores:")
print(scores)

# 1. Add 10 marks to every score
print("\nAfter Adding 10 Marks:")
print(scores + 10)

# 2. Multiply every score by 2
print("\nAfter Multiplying by 2:")
print(scores * 2)

# 3. Print only scores greater than 70
print("\nScores Greater Than 70:")
print(scores[scores > 70])

# 4. Print only scores less than 50
print("\nScores Less Than 50:")
print(scores[scores < 50])

# 5. Check which scores are greater than or equal to 60
print("\nScores >= 60:")
print(scores >= 60)