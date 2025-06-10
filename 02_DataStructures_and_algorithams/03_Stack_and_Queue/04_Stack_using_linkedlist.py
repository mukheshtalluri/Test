class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def __str__(self):
        result = ''
        temp_node = self.top
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <--> '
            temp_node = temp_node.next
        return result

    def push_value(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop_value(self):
        if self.height == 0:
            return None
        temp_node = self.top
        self.top.next = self.top
        temp_node.next = None
        self.height -= 1

    def peek_value(self):
        return self.top

    def is_empty(self):
        if self.height == 0:
            return True
        return False

    def size_of_stack(self):
        return self.height

    def clear_stack(self):
        self.top = None
        self.bottom = None
        self.height = 0

