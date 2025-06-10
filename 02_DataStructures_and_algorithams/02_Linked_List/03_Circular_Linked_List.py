class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        result = ''
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node.next == self.head:
                break
            result += ' --> '
        self.length += 1

    def append_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend_value(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def pop_value(self):
        temp_node = self.head
        while temp_node.next is not self.tail:
            temp_node = temp_node.next
        temp_node.next = None
        self.tail = temp_node
        self.tail.next = self.head
        self.length -= 1
        return temp_node.next

    def pop_first_value(self):
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        self.tail.next = self.head
        self.length -= 1
        return temp_node