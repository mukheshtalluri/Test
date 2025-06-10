def linear_search(input_list, target_value):
    for i in range(len(input_list)):
        if input_list[i] == target_value:
            return f'value found at index : {i}'
    return 'value not found'

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(my_list, 22))