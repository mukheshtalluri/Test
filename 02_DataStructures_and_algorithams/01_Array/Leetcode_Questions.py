# Leetcode array related questions

# Easy level
# Leetcode - 1 : Two Sum - Hashmap based lookup
def two_sum(nums, target):
    nums_dict = {}
    for i, val in enumerate(nums):
        target_value = target - val
        if target_value in nums_dict:
            return nums_dict[target_value], i
        else:
            nums_dict[val] = i

# Leetcode - 121 : Best time to buy and sell stocks - Track min value and max profit
def best_time_to_buy_and_sell_stocks(prices):
    min_value = float('inf')
    max_profit = 0
    for i in prices:
        if i < min_value:
            min_value = i
        profit = i - min_value
        if profit > max_profit:
            max_profit = profit
    return max_profit

# Leetcode - 26 : Remove duplicated from sorted array - Two-pointer approach
def remove_duplicates_from_sorted_array(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return nums

# Leetcode - 88 : Merged sorted array - In-place from the end
def merged_sorted_array(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    return nums1

#Leetcode - 217 : Contain duplicate - Use set for the lookup
def contain_duplicate(nums):
    nums_set = set()
    for i in nums:
        if i in nums_set:
            return True
        else:
            nums_set.add(i)
    return False

# Medium level
# Leetcode - 15 : Three sum - Two pointer + sorting
def three_sum(nums):
    result = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result

# Leetcode - 238 : Product of array except self - Prefix and suffix multiplication
def product_of_array_except_self(nums):
    ...

# Leetcode - 560 : Subarray sum equals to K - Prefix sum + hashmap
def prefix_sum(nums):
    ...

# Leetcode - 73 : Set matrix zeros - Use first row/ column as markers
def set_matrix_zeros(nums):
    ...

# Leetcode - 57 : Insert interval - Merge intervals smartly
def insert_interval():
    ...

# Hard level
# Leetcode - 41 : First missing positive - In-place bucket sort
def first_missing_positive():
    ...

# Leetcode - 23 : Merged k sorted arrays / Lists - Min heap approach
def merged_k_sorted_arrays():
    ...

# Leetcode - 42 : Trapping rain water - Two pointers or precompute max heights
def trapping_rain_water():
    ...

# Leetcode - 1186 : Maximum subarray sum with one deletion - Dynamic programing
def maximum_subarray_sum_with_one_deletion():
    ...

# Leetcode - 689 : Maximum sum of 3 non-overlapping subarrays - Sliding window + Dynamic programing
def maximum_sum_of_3_non_overlapping_subarrays():
    ...


if __name__ == "__main__":
    #print(two_sum([1, 2, 3, 4, 5], 8))
    #print(best_time_to_buy_and_sell_stocks([1, 2, 3, 4, 5, 6, 7, 8]))
    #print(remove_duplicates_from_sorted_array([1, 2, 2, 3, 4, 5, 5]))
    #print(merged_sorted_array([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3 ))
    #print(contain_duplicate([1, 2, 3, 1]))
    print(three_sum([-1,0,1,2,-1,-4]))