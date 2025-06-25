"""
    Bubble sort :
        Bubble sort is a brute force algorithm in which every iteration will move the largest element to end of list.
            - Time complexity - O(n ^ 2)
            - Space complexity - O(1)
"""
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))