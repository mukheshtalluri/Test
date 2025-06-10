def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list

my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(insertion_sort(my_list))