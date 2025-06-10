# Tree : Tree is a non-linear data structure used to store the elements in a hierarchical relation.

class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self, level = 0):
        result = ' ' * level + str(self.data) + '\n'
        for child in self.children:
            result += child.__str__(level + 2)
        return result

    def add_child(self, Tree):
        return self.children.append(Tree)

drinks = Tree('Drinks')
cold = Tree('Cold')
hot = Tree('Hot')
cola = Tree('Cola')
fanta    = Tree('Fanta')
coffee = Tree('Coffee')
tea = Tree('Tea')
drinks.add_child(cold)
drinks.add_child(hot)
cold.add_child(cola)
cold.add_child(fanta)
hot.add_child(coffee)
hot.add_child(tea)
print(drinks)