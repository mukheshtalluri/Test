"""
    Knapsack Problem : The problem which will contain some weights and associated values we need take the weights which will less than the target weight and value should be most.
"""
# Knapsack problem : Bottom Up DP
def knapsack(weights, values, target_weight):
    n = len(weights)

    dp = [[0] * (target_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(target_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][target_weight]

# Knapsack optimised
def knapsack_optimised(weights, values, target_weight):
    n = len(weights)
    dp = [0] * (target_weight + 1)
    for i in range(n):
        for w in range(target_weight, weights[i] -1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[target_weight]

# Knapsack brute force
def knapsack_bruteforce(weights, values, capacity):
    if not weights or capacity == 0:
        return 0
    if weights[0] > capacity:
        return knapsack_bruteforce(weights[1:], values[1:], capacity)

    include = values[0] + knapsack_bruteforce(weights[1:], values[1:], capacity - weights[0])
    exclude = knapsack_bruteforce(weights[1:], values[1:], capacity)
    return max(include, exclude)

values = [60, 100, 120]
weights = [10, 20, 30]
target_value = 50
print(knapsack_bruteforce(weights, values, target_value))
