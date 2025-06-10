# Leetcode - 704 | TC - O(log n), SC - O(1)
# Binary search : We have array of elements we need find an element with logarithmic time complexity.
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return f'Element {target} found at index of {mid}'
    return 'Element not found'

# Leetcode - 74 | TC - O(log n), SC - O(1)
# Search in 2D matrix : We have matrix of elements along with the target value. if target value persent in the matrix we need to return True else False.
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        mid_value = matrix[row][col]
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Leetcode - 875
# Koko eating bananas:
def min_eating_speed(piles, h):
    left, right = 0, max(piles)
    result = right
    while left <= right:
        mid = (left + right) // 2
        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + mid - 1) // mid
        if hours_needed <= h:
            result = mid
            right = mid -1
        else:
            left = mid + 1
    return result

# Leetcode - 153
# Find minimum in rotated sorted arrays :
def minimum_in_rotated_array(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Leetcode - 33
# Search in rotated sorted array:
def search_in_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return f'Element {target} found at the index of {mid}'
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return 'Element not found'

# Leetcode - 981
# Time based key-value store :

# Leetcode - 4
# Median of two sorted arrays :
def median_of_two_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m



if __name__ == '__main__':
    #print(binary_search([-1,0,3,5,9,12], 9))
    #print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    #print(min_eating_speed([30, 11, 23, 4, 20], 6))
    #print(minimum_in_rotated_array([4,5,6,7,0,1,2]))
    print(search_in_rotated_array([4,5,6,7,0,1,2], 1))