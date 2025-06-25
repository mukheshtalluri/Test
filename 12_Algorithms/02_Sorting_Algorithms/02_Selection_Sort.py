"""
    Selection sort :
        Selection sort is a sorting technique which work based on the try to a find minimum value in the list and place in the appropriate position.
            - Time complexity - O(n ^ 2)
            - Space complexity - O(1)
"""
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums

print(selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))