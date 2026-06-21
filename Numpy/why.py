#arr= [85, 92, 78, 95, 88]

import numpy as np
arr = np.array([85, 92, 78, 95, 88]) #NumPy can process millions of numbers much faster
print(arr)

arr = np.array([  #2D array
    [1, 2, 3],
    [4, 5, 6]
])

arr = np.array([ #3D array
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])


print(arr.shape)  #gives rows and coloumns
print(arr.ndim)   #tells dimensions (2d or 3d)
print(arr.size)   #Total elements
print(arr.dtype)

print(arr[0]) #first row
print(arr[-1]) #last row

arr[row][column] #particular element
print(arr[0:3]) #first three elements  start : stop stop not included
print(arr[::2])  #[start : stop : step]
