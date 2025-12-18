import numpy as np

# Creating NumPy Arrays
print("Creating NumPy Arrays:")
# From a list
arr1 = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr1)
# Zeros array
arr2 = np.zeros((3, 3))
print("Zeros array:\n", arr2)
# Ones array
arr3 = np.ones((2, 4))
print("Ones array:\n", arr3)
# Random array
arr4 = np.random.rand(2, 3)
print("Random array:\n", arr4)
print()

# NumPy Array Indexing and Slicing
print("NumPy Array Indexing and Slicing:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n", arr)
# Indexing
print("Element at [1,2]:", arr[1, 2])
# Slicing
print("First row:", arr[0, :])
print("First column:", arr[:, 0])
print("Subarray [0:2, 1:3]:\n", arr[0:2, 1:3])
print()

# Reshaping and Resizing Arrays
print("Reshaping and Resizing Arrays:")
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D array:", arr)
# Reshape
reshaped = arr.reshape(2, 3)
print("Reshaped to 2x3:\n", reshaped)
# Resize (in-place)
arr.resize(3, 2)
print("Resized to 3x2:\n", arr)
print()

# Stacking and Splitting Arrays
print("Stacking and Splitting Arrays:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Vertical stack
vstacked = np.vstack((a, b))
print("Vertical stack:\n", vstacked)
# Horizontal stack
hstacked = np.hstack((a, b))
print("Horizontal stack:", hstacked)
# Split
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)
print("Split into 3:", split_arr)
print()

# Broadcasting
print("Broadcasting:")
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
print("Array a:", a)
print("Array b:\n", b)
# Broadcasting addition
result = a + b
print("Broadcasted addition (a + b):\n", result)

