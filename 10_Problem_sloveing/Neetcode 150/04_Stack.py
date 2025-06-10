# Leetcode - 20 | TC - O(n), SC - O(n)
# Valid parenthesis : We have list of parenthesis need to return true if those are placed in correct order else return false.
def valid_parenthesis(string):
    stack = []
    mapping = {'}' : '{', ')' : '(', ']' : '['}
    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return len(stack) == 0

# Leetcode - 155 | TC - O(1), SC - O(n)
# Min stack : Design a min stack with push, pop, top, get_min with the constant time.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push_value(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    def pop_value(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.min_stack[-1]:
                self.min_stack.pop()
    def top_value(self):
        if self.stack:
            return self.stack[-1]
        return None
    def get_min_value(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Leetcode - 150 | TC - O(n), SC - O(n)
# Evaluate reverse polish notation : We have list of numbers along with some mathematical symbols we need to do mathematical calculations.
def evaluate_reverse_polish_notation(tokens):
    stack = []
    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

# Leetcode - 22
# Generate parenthesis : We have number as argument, and we write a function to well-formed parenthesis.
def generate_parenthesis(num):
    result = []
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * num:
            result.append(current)
            return
        if open_count < num:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    backtrack('', 0, 0)
    return result

# Leetcode - 739
# Daily temperatures : We have array of temperatures we need how many days to get warmer temperatures.
def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result

# Leetcode - 853
# Car fleet :
def car_fleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

# Leetcode - 84
# Largest rectangle in histogram : We have array of numbers we need to return the max rectangle area in the histogram.
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, width * height)
        stack.append(i)
    return max_area


if __name__ == '__main__':
    #print(valid_parenthesis('([])'))
    #print(evaluate_reverse_polish_notation(["10", "6", "9", "3", "/", "-", "*"]))
    #print(generate_parenthesis(3))
    #print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    #print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print(largest_rectangle_area([2,1,5,6,2,3]))