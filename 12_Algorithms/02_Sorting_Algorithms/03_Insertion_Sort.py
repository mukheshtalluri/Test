"""
    Insertion sort :
        Insertion sort is a sorting technique it will compare the values and sort them.
            - Time complexity - O(n ^ 2)
            - Space complexity - O(1)
"""
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))