# Binary Tree
class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self, level = 0):
        result = " " * level + str(self.data) + '\n'
        for child in self.children:
            result += child.__str__(level + 2)
        return result

    def add_children(self, Tree):
        return self.children.append(Tree)