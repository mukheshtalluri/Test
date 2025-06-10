# Linked list is a sequential data structure and elements are not stored in the order index.

# Node : Node is an element which consist of value and reference to the next node.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list and its methods
class SingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        result = ''
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

    def empty_linked_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_value(self):
        if self.head is None:
            return None
        pre_node = self.head
        temp_node = self.head
        while temp_node.next:
            pre_node = temp_node
            temp_node = temp_node.next
        self.tail = pre_node
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp_node.value

    def pop_first_value(self):
        if self.head is None:
            return None
        temp_node = self.head
        self.head = temp_node.next
        temp_node.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp_node.value

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node

    def set_value(self, index, value):
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert_value(self, index, value):
        new_node = Node(value)
        if index < 0  or index > self.length:
            return None
        if index == 0:
            return self.prepend_value(value)
        elif index == self.length:
            return self.append_value(value)
        else:
            temp_node = self.get_value(index - 1)
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def remove_value(self, index):
        if index < 0  or index >= self.length:
            return None
        if index == 0:
            return self.pop_first_value()
        elif index == self.length:
            return self.pop_value()
        else:
            pre_node = self.get_value(index - 1)
            temp_node = self.get_value(index)
            pre_node.next = temp_node.next
            temp_node.next = None
        self.length -= 1
        return temp_node

    def reverse_linked_list(self):
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node
        after = temp_node.next
        before = None
        for _ in range(self.length):
            after = temp_node.next
            temp_node.next = before
            before = temp_node
            temp_node = after


single_linked_list = SingleLinkedList(16)
single_linked_list.append_value(25)
single_linked_list.prepend_value(7)
single_linked_list.append_value(34)
single_linked_list.append_value(43)
single_linked_list.append_value(52)
single_linked_list.append_value(61)
single_linked_list.append_value(70)
print(single_linked_list)
single_linked_list.reverse_linked_list()
print(single_linked_list)
