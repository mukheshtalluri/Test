def bubble_sort(input_list):
    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(bubble_sort(my_list))