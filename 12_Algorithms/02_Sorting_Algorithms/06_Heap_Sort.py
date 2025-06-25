"""
    Heapify sort :
        Heap sort is a sorting algorithm.
            - Time complexity - O(n log n)
            - Space complexity - O(1)
"""
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(nums):
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    for i in range(n -1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
heap_sort(array)
print(array)




