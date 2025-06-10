class Queue:
    def __init__(self):
        self.values = []

    def __str__(self):
        result = ''
        for i in range(len(self.values)):
            result += str(self.values[i])
            if i != len(self.values) - 1:
                result += ' <--> '
        return result

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        self.values.pop(0)

    def peek(self):
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def size_of_queue(self):
        return len(self.values)

    def clear_queue(self):
        self.values.clear()

queue = Queue()
print(queue)

