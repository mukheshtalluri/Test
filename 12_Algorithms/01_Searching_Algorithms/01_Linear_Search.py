"""
    Linear Search :
        Linear Search is a Brute force algorithm. We can search for an element in every possible way.
            - Time complexity : O(n)
            - Space complexity : O(1)
"""

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return f'Element found at the index of {i}.'
    return f'Element not found.'

print(linear_search([1, 2, 3, 4, 5, 6, 7, 8], 5))