# Leetcode - 217 | TC - O(n), SC - O(1)
# Contain duplicate : We have array of elements, we need to return true if elements are repeated else return false.
def contain_duplicate(nums):
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
        unique_nums.add(num)
    return False

# Leetcode - 242 | TC - O(n), SC - O(1)
# Valid anagram : We have two strings, occurrence of the elements in the both the strings are same we need to return true else false.
def valid_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    count = [0] * 26
    for i in range(len(string1)):
        count[ord(string1[i]) - ord('a')] += 1
        count[ord(string2[i]) - ord('a')] -= 1
    return all(x == 0 for x in count)

# Leetcode - 1 | TC - O(n), SC - O(1)
# Two sum : We have array of elements and target element, we need to return index of position of element whose sum equal to target.
def two_sum(nums, target):
    num_dict = {}
    for i, val in enumerate(nums):
        target_element = target - val
        if target_element in num_dict:
            return num_dict[target_element], i
        num_dict[val] = i

# Leetcode - 49 | TC - O(n * m), SC - O(n)
# Group anagram : We have list of words, we need group them according to their occurrence.
def group_anagram(words):
    anagram_group = {}
    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        if key not in anagram_group:
            anagram_group[key] = []
        anagram_group[key].append(word)
    return list(anagram_group.values())

# Leetcode - 347 | TC - O(n), SC - O(n)
# Top k frequent elements : we have array of elements and k value, we need to return the top k most elements in the array.
def top_k_frequent_elements(nums, k):
    num_dict = {}
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, freq in num_dict.items():
        bucket[freq].append(num)
    result = []
    for i in range(len(bucket) -1, -1, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

# Leetcode - 238 | TC - O(n), SC - O(n)
# Product of array except self : We have array of elements, we need to result array which having product of other elements excepts self.
def product_array_except_self(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) -1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result

# Leetcode - 36
# Valid sudoku : We have 2d array which is in the form of matrix. we need to return true if its valid sudoku else false.
def valid_sudoku(nums):
    ...

# Leetcode - Private
# Encode and Decode of strings : We have list of words. we encode them and return encoded result. again if we pass the encoded result decode method need to decode and return the result.
def encode(words):
    return '#'.join(words)

def decode(string):
    return string.split('#')

# Leetcode - 128 | TC - O(n), SC - O(n)
# Longest consecutive subsequence : We have array of numbers we need to return their consecutive subsequence.
def longest_consecutive_subsequence(nums):
    num_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)
    return longest


if __name__ == '__main__':
    #print(contain_duplicate([1, 2, 3, 1]))
    #print(valid_anagram('car', 'rac'))
    #print(two_sum([2, 7, 11, 15], 9))
    #print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
    #print(top_k_frequent_elements([1,1,1,2,2,3], 2))
    #print(product_array_except_self([1, 2, 3, 4]))
    #encoded_string = encode(['apple', 'ball', 'cat'])
    #print(decode(encoded_string))
    print(longest_consecutive_subsequence([100,4,200,1,3,2]))
