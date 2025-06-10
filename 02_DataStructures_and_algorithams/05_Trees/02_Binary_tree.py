# BinaryTree :
from queue import Queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

binary_tree = BinaryTree('Drinks')
cold = BinaryTree('Cold')
hot = BinaryTree('Hot')
cola = BinaryTree('Cola')
fanta = BinaryTree('Fanta')
coffee = BinaryTree('Coffee')
tea = BinaryTree('Tea')
binary_tree.left_child = cold
binary_tree.right_child = hot
cold.left_child = cola
cold.right_child = fanta
hot.left_child = coffee
hot.right_child = tea

# pre-order search
def pre_order_search(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_search(root_node.left_child)
    pre_order_search(root_node.right_child)

# level-order search
def level_order_search(root_node):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        print(root.data)
        if root.left_child is not None:
            custom_queue.put(root.left_child)
        if root.right_child is not None:
            custom_queue.put(root.right_child)

# search value
def search_value(root_node, value):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        if root.data == value:
            return f'Value {value} found'
        if root.left_child:
            custom_queue.put(root.left_child)
        if root.right_child:
            custom_queue.put(root.right_child)
    return f'Value {value} not found'

# insert node
def insert_node(root_node, new_node):
    if not root_node:
        root_node = new_node
        return 'new_node inserted at the root.'
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        if not root.left_child:
            root.left_child = new_node
            return f'Inserted {new_node.data} is left of the {root.data}'
        else:
            custom_queue.put(root.left_child)
        if not root.right_child:
            root.right_child = new_node
            return f'Inserted {new_node.data} is right of the {root.data}'
        else:
            custom_queue.put(root.right_child)

# get deep node
def get_deep_node(root_node):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        if root.left_child:
            custom_queue.put(root.left_child)
        if root.right_child:
            custom_queue.put(root.right_child)
    return root

# delete deep node
def delete_deep_node(root_node, deep_node):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        if root.left_child:
            if root.left_child == deep_node:
                root.left_child = None
                return 'Deep node is deleted'
            else:
                custom_queue.put(root.left_child)
        if root.right_child:
            if root.right_child == deep_node:
                root.right_child = None
                return 'Deep node is deleted'
            else:
                custom_queue.put(root.right_child)

# delete node
def delete_node(root_node, value):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        if root.data == value:
            deep_node = get_deep_node(root_node)
            root.data = deep_node.data
            delete_deep_node(root_node, deep_node)
            return 'Node is deleted successfully'
        if root.left_child:
            custom_queue.put(root.left_child)
        if root.right_child:
            custom_queue.put(root.right_child)

# delete binary tree
def delete_binary_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return 'BinaryTree is deleted successfully.'




