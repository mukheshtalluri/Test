"""
    Quick sort:
        Quick sort is a sorting technique which uses divide and conquer algorithm. It will take pivot value as reference and sort the value based on pivot value.
            - Time complexity - O(n log n)
            - Space complexity - O(1)
"""
def quick_sort(nums):
    if len(nums) < 1:
        return nums
    mid = len(nums) // 2
    pivot = nums[mid]
    left_part = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right_part = [x for x in nums if x > pivot]
    return quick_sort(left_part) + mid + quick_sort(right_part)

print(quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))