"""
    Fibonacci sequence :
        Fibonacci sequence is the sequence of numbers which is sum of 2 previous numbers.
"""
# Top - Down DP (Memoization with Recursion) - Time complexity : O(n), Space complexity : O(n)
def fib_memo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(10))

# Bottom - Up DP (Tabulation with Iteration) - Time complexity : O(n), Space complexity : O(n)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fib_tab(10))

# Bottom - Up DP with Optimisation - Time complexity : O(n), Space complexity : O(1)
def fib_optimised(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fib_optimised(10))