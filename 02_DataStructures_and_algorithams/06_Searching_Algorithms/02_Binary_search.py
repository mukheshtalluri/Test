def binary_search(input_list, target_value):
    left, right = 0, len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] > target_value:
            right = mid - 1
        elif input_list[mid] < target_value:
            left = mid + 1
        else:
            return f'value found at index : {mid}'
    return 'value not found'

my_list = [0, 2, 4, 6, 8, 10]
print(binary_search(my_list, 10))