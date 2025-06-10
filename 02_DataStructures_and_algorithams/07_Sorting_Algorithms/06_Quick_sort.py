def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[len(input_list) // 2]

    left_part = [x for x in input_list if x < pivot]
    middle = [x for x in input_list if x == pivot]
    right_part = [x for x in input_list if x > pivot]

    return quick_sort(left_part) + middle + quick_sort(right_part)

my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(quick_sort(my_list))