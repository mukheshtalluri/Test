from array import *

# Creating array using array module
my_array = array('i', [1, 2, 3, 4, 5, 6])
print('Array elements : ', my_array)


# Print all elements in an array
for i in range(len(my_array)):
    print(f'element at {i} index : {my_array[i]}')

# Appending method : Add element at the end of an array
my_array.append(7)
print('Array elements : ', my_array)

# Insert method : Insert element into the array - Edge case : If provided index greater than the last index value will be inserted at the last index.
my_array.insert(7, 8)
print('Array elements : ', my_array)

# Extend method : Add iterable to the array
my_array_1 = array('i', [9, 10])
my_array.extend(my_array_1)
print('Array elements : ', my_array)

# Remove method : Remove element from the list - If the value try to remove not in the array will through type error.
my_array.remove(10)
print('Array elements : ', my_array)

# Count method : Count method will count the occurrence of element
print(f'The element {5} repeated {my_array.count(5)} times in the array.')

# Pop method : Pop method will remove the end of element from an array and if you provide any index it will remove value in that index position.
print(my_array.pop()) # Remove last element from the array
print(my_array.pop(3)) # Remove element which is in 3 index
print('Array elements : ', my_array)

# Index method : Index method will return the index position of element in array
print(my_array.index(7))

# Reverse method : Reverse method will reverse the order of element in an array
my_array.reverse()
print('Array elements : ', my_array)

# Tolist method : Tolist method will convert the array to the list
my_list = my_array.tolist()
print(type(my_list))
print(type(my_array))






