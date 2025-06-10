def selection_sort(input_list):
    for i in range(len(input_list) - 1):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list


my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(selection_sort(my_list))