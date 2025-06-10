# Leetcode - 125 | TC - O(n), SC - O(1)
# Valid palindrome : We have given string, we need to return true if it is palindrome else return false.
def valid_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        while left < right and not string[left].isalnum():
            left += 1
        while left < right and not string[right].isalnum():
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Leetcode - 167 | TC - O(n), SC - O(1)
# Two sum - II : We have array of nums and target element, we need to return index position of elements whose sum equal to target.
def two_sum_2(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        element_sum = nums[left] + nums[right]
        if element_sum > target:
            right -= 1
        elif element_sum < target:
            left += 1
        else:
            return left, right

# Leetcode - 15 | TC - O(n ^ 2), SC - O(1)
# Three sum : We have array of elements, we need to consider 3 elements whose sum equal to zero and three are not equal.
def three_sum(nums):
    result = []
    nums.sort()
    for i, val in enumerate(nums):
        if i > 0 and val == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            element_sum = val + nums[left] + nums[right]
            if element_sum > 0:
                right -= 1
            elif element_sum < 0:
                left += 1
            else:
                result.append([val, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

# Leetcode - 11 | TC - O(n), SC - O(1)
# Container with most water : We have array of heights which can store quantity of water we need to return the maximum quantity.
def container_with_most_water(heights):
    max_quantity = 0
    left, right = 0, len(heights) - 1
    while left < right:
        if heights[left] < heights[right]:
            quantity = heights[left] * (right - left)
            left += 1
        else:
            quantity = heights[right] * (right - left)
            right -= 1
        max_quantity = max(quantity, max_quantity)
    return max_quantity

# Leetcode - 42 | TC - O(n), SC - O(1)
# Trapped rain water : We have array of heights based on their heights rain water store between heights need to calculate quantity of water.
def trapped_rain_water(heights):
    total = 0
    max_left_height = 0
    max_right_height = 0
    left, right = 0, len(heights) - 1
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > max_left_height:
                max_left_height = heights[left]
            if max_left_height - heights[left] > 0:
                total += max_left_height - heights[left]
            left += 1
        else:
            if heights[right] > max_right_height:
                max_right_height = heights[right]
            if max_right_height - heights[right] > 0:
                total += max_right_height - heights[right]
            right -= 1
    return total


if __name__ == '__main__':
    #print(valid_palindrome('A man, a plan, a canal: Panama'))
    #print(two_sum_2([2, 7, 11, 15], 9))
    #print(three_sum([-1,0,1,2,-1,-4]))
    #print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
    print(trapped_rain_water([4,2,0,3,2,5]))