class Stack:
    def __init__(self):
        self.values = []

    def __str__(self):
        result = ''
        for i in range(len(self.values)):
            result += str(self.values[i])
            if i != len(self.values) - 1:
                result += ' <--> '
        return result

    def push_value(self, value):
        self.values.append(value)

    def pop_value(self):
        self.values.pop()

    def peek_element(self):
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def size_of_stack(self):
        return len(self.values)

    def clear_stack(self):
        self.values.clear()