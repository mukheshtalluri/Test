from numpy import *

# Create two-dimensional array using numpy
my_array = array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print('Elements in an array : ', my_array)

# Print all elements in an array
for i in range(len(my_array)):
    for j in range(len(my_array[i])):
        print(my_array[i][j])

# Append method : Append method will add elements at the end of an array - If axis = 0 it will consider as row and 1 it will consider as column
my_array = append(my_array,[[10, 11, 12]], axis=0)
print(my_array)

# Insert method : Insert method will add elements in specified row or column.
my_array = insert(my_array, 3, [13, 14, 15], axis=0)
print(my_array)

# Delete method : Delete method will delete the elements of row or column in an array
my_array = delete(my_array, 0, axis=0)
print(my_array)


