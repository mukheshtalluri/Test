# Factorial of number
def factorial_number(num):
    assert 0 <= num == int(num), 'Input number should be non negative integer only.'
    if num in [0, 1]:
        return 1
    return num * factorial_number(num - 1)

# Fibonacci sequence
def fibonacci_sequence(num):
    assert 0 <= num == int(num), 'Input number should be non negative integer only.'
    if num in [0, 1]:
        return num
    return fibonacci_sequence(num - 2) + fibonacci_sequence(num - 1)

# Sum of digits
def sum_of_digits(num):
    assert 0 <= num == int(num), 'Input number should be non negative integer only.'
    if num <= 9:
        return num
    return num % 10 + sum_of_digits(num // 10)

# Reverse string
def reverse_string(string):
    assert len(string) > 0, 'String length should be more than one.'
    if len(string) == 1:
        return string
    return string[-1] + reverse_string(string[:-1])

# Palindrome string
def palindrome_string(string):
    assert len(string) > 0, 'String length should be more than one.'
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome_string(string[1 : -1])
    return False

# Count zeros in a number
def count_zeros(num):
    if num == 0:
        return 1
    if num < 10:
        return 1 if num == 0 else 0
    return (1 if num % 10 == 0 else 0) + count_zeros(num // 10)

# Print numbers from n to 1
def print_numbers_n_to_1(num):
    if num == 0:
        return
    print(num)
    print_numbers_n_to_1(num - 1)

# Print numbers from 1 to n
def print_numbers_1_to_n(num, current = 1):
    if num < current:
        return
    print(current)
    print_numbers_1_to_n(num, current + 1)

# Power of number
def power_of_num(num, power):
    if power == 0:
        return 1
    return num * power_of_num(num, power - 1)

# Tribonacci series
def tribonacci_series(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return tribonacci_series(num - 1) + tribonacci_series(num - 2) + tribonacci_series(num - 3)

# Subsequence
def subsequence(string):
    if not string:
        return ['']
    first = string[0]
    rest = subsequence(string[1:])
    return rest + [first + sub for sub in rest]

# Subset sum problem
def subset(nums, target, index = 0, current = []):
    if index == len(nums):
        if sum(current) == target:
            return [current[:]]
        return []
    include = subset(nums, target, index + 1, current + [nums[index]])
    exclude = subset(nums, target, index + 1, current)
    return include + exclude



if __name__ == '__main__':
    #print(factorial_number(3))
    #print(fibonacci_sequence(3))
    #print(sum_of_digits(1234))
    #print(reverse_string('mukhesh'))
    #print(palindrome_string('madam'))
    #print(count_zeros(10))
    #print(print_numbers_n_to_1(10))
    #print(print_numbers_1_to_n(10))
    #print(power_of_num(2, 5))
    #print(tribonacci_series(5))
    #print(subsequence('abcd'))
    print(subset([1, 2, 3], 3))