class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def __str__(self):
        result = ''
        temp_node = self.first
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <--> '
            temp_node = temp_node.next
        return result

    def enqueue_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue_value(self):
        if self.length == 0:
            return
        temp_node = self.first
        self.first.next = self.first
        temp_node.next = None
        self.length -= 1

    def peek_element(self):
        if self.length == 0:
            return
        return self.first

    def length_of_queue(self):
        if self.length == 0:
            return
        return self.length

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def clear_queue(self):
        self.first = None
        self.last = None
        self.length = 0

