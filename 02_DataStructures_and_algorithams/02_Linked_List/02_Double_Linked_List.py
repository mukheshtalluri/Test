class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
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
                result += ' <--> '
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop_value(self):
        temp_node = self.tail
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp_node.prev
            self.tail.next = None
            temp_node.prev = None
        self.length -= 1
        return temp_node.value

    def pop_first_value(self):
        temp_node = self.head
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp_node.next = None
        self.length -= 1
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
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend_value(value)
        elif index == self.length:
            return self.append_value(value)
        else:
            pre_node = self.get_value(index - 1)
            temp_node = self.get_value(index)
            pre_node.next = new_node
            new_node.next = temp_node
            temp_node.prev = new_node
            new_node.prev = pre_node
        self.length += 1

    def remove_value(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first_value()
        elif index == self.length -1:
            return self.pop_value()
        else:
            pre_node = self.get_value(index - 1)
            temp_node = self.get_value(index)
            pre_node.next = temp_node.next
            temp_node.next.prev = pre_node
            temp_node.next = None
            temp_node.prev = None
        self.length -= 1
        return temp_node.value

double_linked_list = DoubleLinkedList(16)
double_linked_list.append_value(25)
double_linked_list.prepend_value(7)
double_linked_list.append_value(34)
double_linked_list.append_value(43)
double_linked_list.append_value(52)
double_linked_list.append_value(61)
double_linked_list.append_value(70)
double_linked_list.remove_value(8)
print(double_linked_list)
