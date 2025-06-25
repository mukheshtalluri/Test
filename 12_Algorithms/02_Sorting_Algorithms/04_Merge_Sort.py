"""
    Merge sort :
        Merge sort is a sorting technique which work based on divided and conquer algorithm. Initially whole list divided into equal half's and merge them with respect to sort.
            - Time complexity - O(n log n)
            - Space complexity - O(n)
"""
def merge_sort(nums):
    n = len(nums)
    if n > 1:
        mid = len(nums) // 2
        left_part = nums[:mid]
        right_part = nums[mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        i = 0
        j = 0
        k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                nums[k] = left_part[i]
                i += 1
            else:
                nums[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            nums[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            nums[k] = right_part[j]
            j += 1
            k += 1
        return nums

print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))


