import numpy as np

arr = np.array([85, 92, 78, 95, 88,64])
arr.resize(2,3)    #changes array into matrix
                
arr1=np.array([85, 92, 78, 95, 88])     
arr1.reshape(5, 1) #incase of odd numbers it can be converted to one row or coloumn matrix

arr2 = np.array([1,2,3,4,5,6])
arr2.reshape(2,-1) #numpy figure out the number of coloumns on it's number
arr2T=arr2.T #makes transpose

matrix = np.array([
    [1,2,3],
    [4,5,6]
])
flat=matrix.flatten() #matrix to array

print(arr)

print(arr1)

print(arr2) 

print(flat)
