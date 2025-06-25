"""
🔹 Array and String
    - Two Sum

    -> Brute force : Time complexity - O( n ^ 2), Space complexity - O(1)
        def two_sum(nums, target):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]

        print(two_sum([2, 7, 11, 15], 9))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(n)
        def two_sum(nums, target):
            seen = {}
            for i, val in enumerate(nums):
                search = target - val
                if search in seen:
                    return [seen[search], i]
                seen[val] = i

        print(two_sum([2, 7, 11, 15], 9))

    - Best Time to Buy and Sell Stock

    -> Brute force : Time complexity - O( n ^ 2), Space complexity - O(1)
        def best_time_to_buy_sell_stocks(prices):
            max_profit = 0
            for i in range(len(prices)):
                for j in range(i + 1, len(prices)):
                    profit = prices[j] - prices[i]
                    max_profit = max(profit, max_profit)
            return max_profit

        print(best_time_to_buy_sell_stocks([7, 1, 5, 3, 6, 4]))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(1)
        def best_time_to_buy_sell_stocks(prices):
            min_price = float('inf')
            max_profit = 0
            for price in range(len(prices)):
                if price < min_price:
                    min_price = price
                else:
                    max_profit = max(max_profit, price - min_price)
            return max_profit

        print(best_time_to_buy_sell_stocks([7, 1, 5, 3, 6, 4]))


    - Maximum Subarray (Kadane’s Algorithm)
    -> Brute force : Time complexity - O( n ^ 2), Space complexity - O(1)
        def max_sum_subarray(nums):
            max_sum = float('-inf')
            for i in range(len(nums)):
                current_sum = 0
                for j in range(i, len(nums)):
                    current_sum += nums[j]
                    max_sum = max(current_sum, max_sum)
            return max_sum

        print(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(1)
        def max_sum_subarray(nums):
            max_sum = cur_sum = nums[0]
            for num in nums[1:]:
                cur_sum = max(num, cur_sum + num)
                max_sum = max(max_sum, cur_sum)
            return max_sum

        print(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    - Merge Intervals
    -> Brute force : Time complexity - O(n ^ 2), Space complexity - O(n)
        def merge_intervals(intervals):
            merged = intervals[:]
            i = 0
            while i < len(merged):
                j = i + 1
                while j < len(merged):
                    a, b = merged[i], merged[j]
                    if b[0] <= a[1] and a[0] <= b[1]:
                        merged[i] = [min(a[0], b[0]), max(a[1], b[1])]
                        merged.pop(j)
                        i -= 1
                        break
                    else:
                        j += 1
                i += 1
            return merged

        print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(1)
        def merge_intervals(intervals):
            if not len(intervals):
                return []
            intervals.sort(key=lambda x : x[0])
            merged = [intervals[0]]
            for current in intervals[1:]:
                last = merged[-1]
                if current[0] <= last[1]:
                    last[1] = max(current[1], last[1])
                else:
                    merged.append(current)
            return merged

        print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

    - Longest Substring Without Repeating Characters
    -> Brute force : Time complexity - O(n ^ 2), Space complexity - O(n)
        def longest_substring_without_repeating_characters(string):
            max_len = 0
            for i in range(len(string)):
                for j in range(i, len(string)):
                    sub_string = string[i : j + 1]
                    if len(set(sub_string)) == len(sub_string):
                        max_len = max(max_len, j - i + 1)
            return max_len

        print(longest_substring_without_repeating_characters('abcabcbb'))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(1)
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

        print(longest_substring_without_repeating_characters('abcabcbb'))

    - Product of Array Except Self
    -> Brute force : Time complexity - O(n ^ 2), Space complexity - O(n)
        def product_array_except_self(nums):
            result = []
            for i in range(len(nums)):
                prod = 1
                for j in range(len(nums)):
                    if i != j:
                        prod *= nums[j]
                result.append(prod)
            return result

        print(product_array_except_self([1, 2, 3, 4]))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(1)
        def product_array_except_self(nums):
            result = [0] * len(nums)
            prefix = 1
            for i in range(len(nums)):
                result[i] = prefix
                prefix *= nums[i]
            suffix = 1
            for j in range(len(nums) -1, -1, -1):
                result[j] *= suffix
                suffix *= nums[j]
            return result

        print(product_array_except_self([1, 2, 3, 4]))

    - Rotate Array
    -> Brute force : Time complexity - O(n ^ 2), Space complexity - O(n)
        def rotate_array(nums, k):
            n = len(nums)
            k = k % n
            for _ in range(k):
                last = nums[-1]
                for i in range(n - 1, 0, -1):
                    nums[i] = nums[i - 1]
                nums[0] = last
            return nums

        print(rotate_array([1, 2, 3, 4, 5, 6, 7, 8], 3))

    -> Optimal approach :  Time complexity - O(n), Space complexity - O(1)


    Check if a String is a Palindrome

    Group Anagrams

    Longest Common Prefix

🔹 Linked List
    Reverse a Linked List

    Detect Cycle in a Linked List

    Merge Two Sorted Lists

    Remove Nth Node From End

    Palindrome Linked List

    Add Two Numbers

🔹 Stack and Queue
    Valid Parentheses

    Min Stack

    Daily Temperatures

    Implement Queue using Stacks

    Sliding Window Maximum

🔹 Hashing / HashMap
    Two Sum

    Subarray Sum Equals K

    Longest Consecutive Sequence

    Top K Frequent Elements

    Isomorphic Strings

🔹 Recursion and Backtracking
    Permutations of a String

    N-Queens Problem

    Sudoku Solver

    Subsets

    Combination Sum

    Word Search

🔹 Binary Search
    Binary Search on Sorted Array

    Search in Rotated Sorted Array

    Find Peak Element

    Kth Smallest Element in a Sorted Matrix

    Median of Two Sorted Arrays

🔹 Trees and Graphs
    Inorder / Preorder / Postorder Traversal

    Level Order Traversal

    Lowest Common Ancestor (LCA)

    Diameter of Binary Tree

    Detect Cycle in Graph

    Clone Graph

    Number of Islands

    Word Ladder

🔹 Dynamic Programming (DP)
    Fibonacci Numbers

    Climbing Stairs

    0/1 Knapsack

    Longest Increasing Subsequence

    Coin Change

    House Robber

    Longest Palindromic Substring

    Edit Distance

🔹 Greedy Algorithms
    Activity Selection Problem

    Jump Game

    Gas Station

    Greedy Job Sequencing

    Minimum Number of Platforms Required

🔹 Bit Manipulation
    Single Number

    Find Missing Number

    Count Bits

    Power of Two

🔹 Databases / SQL
    Find Duplicate Records

    Top N Queries

    Self Join (e.g., Find Managers)

    Aggregate Functions with GROUP BY

    Window Functions (RANK, ROW_NUMBER)

🔹 Object-Oriented Programming (OOP)
    Design a Parking Lot

    Design a Library System

    Design a File System

    Design Elevator System

    Design a Chat Application

🔹 System Design (for senior roles)
    Design Twitter

    Design YouTube

    Design URL Shortener

    Design Rate Limiter

    Design Online Bookstore
"""