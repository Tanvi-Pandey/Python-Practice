import numpy as np

arr = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
])

# 1. First row
print("First row:", arr[0,:])

# 2. Last row
print("Last row:", arr[-1,:])

# 3. First column
print("First column:", arr[:,0])

# 4. Last column
print("Last column:", arr[:,-1])

# 5. Element 25
print("Element 25:", arr[1,1])

# 6. Element 45
print("Element 45:", arr[2,2])