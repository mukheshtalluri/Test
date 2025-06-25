"""
    Binary Search :
        Binary Search is a divide and conquer algorithm. In binary search each and every iteration half of elements are removed and while using binary search used for only sorted elements.
            - Time complexity - O(log n)
            - Space complexity - O(1)
"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return f'Element found at the index of {mid}'
    return 'Element not found'

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 6))