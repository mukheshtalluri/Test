# Binary tree using list :

class BinaryTreeList:
    def __init__(self, size):
        self.list = [None] * size
        self.last_used_index = 0

    def insert_value(self, value):
        if self.last_used_index >= len(self.list) - 1:
            return 'BinaryTree is full.'
        self.last_used_index += 1
        self.list[self.last_used_index] = value
        return f'Inserted {value} at the index of {self.last_used_index}'

    def search_value(self, value):
        for i in range(1, self.last_used_index + 1):
            if self.list[i] == value:
                return f'Value {value} found at index {i}'
        return f'Value {value} not found'

    def get_deep_node(self):
        if self.last_used_index == 0:
            return 'Tree is empty'
        return self.list[self.last_used_index]

    def delete_deep_node(self):
        if self.last_used_index == 0:
            return 'Tree is empty'
        deleted_value = self.list[self.last_used_index]
        self.list[self.last_used_index] = None
        self.last_used_index -= 1
        return f'Deep node {deleted_value} deleted.'

    def delete_node(self, value):
        if self.last_used_index == 0:
            return 'Tree is empty'
        for i in range(1, self.last_used_index + 1):
            if self.list[i] == value:
                self.list[i] = self.list[self.last_used_index]
                self.list[i] = None
                self.last_used_index -= 1
                return f'Node {value} deleted'
        return f'Value {value} not found'


