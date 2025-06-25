# Rotate array
# [1, 2, 3, 4, 5, 6, 7, 8] k = 3 -> [6, 7, 8, 1, 2, 3, 4, 5]

def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    def rotate(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    rotate(0, n - 1)
    rotate(0, k - 1)
    rotate(k, n - 1)
    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7, 8], 3))
