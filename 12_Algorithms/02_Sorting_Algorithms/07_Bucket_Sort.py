"""
    Bucket sort :
        Bucket sort is a sorting algorithm.
            - Time complexity : O(n log n)
            - Space complexity : O(1)
"""
def bucket_sort(nums):
    if len(nums) == 0:
        return nums
    min_val = min(nums)
    max_val = max(nums)
    bucket_count = len(nums)
    bucket_range = (max_val - min_val) / bucket_count + 1e-9
    buckets = [[] for _ in range(bucket_count)]
    for num in nums:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))
    return sorted_array


values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
array = bucket_sort(values)
print(array)