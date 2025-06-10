# Leetcode - 121 | TC - O(n), SC - O(1)
# Best time to buy and sell stocks : We have array of stock prices day by day we need to purchase and sell stocks in such way that it will give us maximum profit.
def best_time_to_buy_and_sell_stocks(prices):
    left = 0
    max_profit = 0
    for right in range(1, len(prices)):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
    return max_profit

# Leetcode - 3 | TC - O(n), SC - O(1)
# Longest substring without repeating characters : We have a string in which series of characters we need to return subarray whose characters are not repeated.
def longest_substring_without_repeating_characters(string):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left += 1
        char_set.add(string[right])
        max_len = max(max_len, right - left + 1)
    return max_len

# Leetcode - 424 | TC - O(n), SC - O(1)
# Longest repeating character replacement : We have string along k value in that characters in the string can be replaced by the k amount. we need to max how many times a character repeated.
def longest_repeating_character_replacement(string, k):
    count = [0] * 26
    left = 0
    max_freq = 0
    max_len = 0
    for right in range(len(string)):
        index = ord(string[right]) - ord('A')
        count[index] += 1
        max_freq = max(max_freq, count[index])
        while (right - left + 1) - max_freq > k:
            count[ord(string[left]) - ord('A')] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Leetcode - 567 | TC - O(n), SC - O(1)
# Permutation in string: We have two strings, if one permutation of string1 present in string2 then return true else false.
def permutation_in_string(string1, string2):
    if len(string1) > len(string2):
        return False
    def frequency(string):
        freq = [0] * 26
        for char in string:
            freq[ord(char) - ord('a')] += 1
        return freq
    s1_count = frequency(string1)
    window_freq = frequency(string2[:len(string1)])
    if s1_count == window_freq:
        return True
    for i in range(len(string1), len(string2)):
        start = ord(string2[i - len(string1)]) - ord('a')
        end = ord(string2[i]) - ord('a')
        window_freq[start] -= 1
        window_freq[end] += 1
        if window_freq == s1_count:
            return True
    return False

# Leetcode - 76 | TC - O(n), SC - O(1)
# Minimum window substring : We have two strings we need to find the minimum string which contain all characters in other string.
def minimum_window_substring(string1, string2):
    if len(string2) > len(string1):
        return ''
    string2_freq = {}
    for char in string2:
        string2_freq[char] = string2_freq.get(char, 0) + 1
    left = 0
    matched = 0
    window_freq = {}
    min_len = float('inf')
    result = ''
    for right in range(len(string1)):
        char = string1[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        if char in string2_freq and window_freq[char] == string2_freq[char]:
            matched += 1
        while matched == len(string2_freq):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = string1[left:right + 1]
            left_char = string1[left]
            window_freq[left_char] -= 1
            if left_char in string2_freq and window_freq[left_char] < string2_freq[left_char]:
                matched -= 1
            left += 1
    return result

# Leetcode - 239 | TC - O(n), SC - O(1)
# Sliding window maximum : We have array elements and window size we need to move the window in define size, and we need to return the maximum element from the window.
def sliding_window_maximum(nums, k):
    result = []
    for i in range(len(nums) - k + 1):
        window_max = nums[i]
        for j in range(i + 1, i + k):
            if nums[j] > window_max:
                window_max = nums[j]
        result.append(window_max)
    return result

if __name__ == '__main__':
    #print(best_time_to_buy_and_sell_stocks([7,1,5,3,6,4]))
    #print(longest_substring_without_repeating_characters('abcabcbb'))
    #print(longest_repeating_character_replacement('ABAB', 2))
    #print(permutation_in_string('abc', 'eidbacoo'))
    #print(minimum_window_substring('ADOBECODEBANC', 'ABC'))
    print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))