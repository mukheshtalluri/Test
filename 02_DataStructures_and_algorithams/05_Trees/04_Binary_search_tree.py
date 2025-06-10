# Binary Search Tree :
from queue import Queue
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert_node(root_node, value):
    if not root_node:
        return BinarySearchTree(value)
    if value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = insert_node(root_node.right_child, value)
    return root_node

def search_value(root_node, value):
    if not root_node:
        return 'Value not found'
    if root_node.data == value:
        return 'Value found'
    elif value < root_node.data:
        return search_value(root_node.left_child, value)
    else:
        return search_value(root_node.right_child, value)

def get_deep_node(root_node):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.put(root_node)
    while not custom_queue.empty():
        root = custom_queue.get()
        if root.left_child is not None:
            custom_queue.put(root.left_child)
        if root.right_child is not None:
            custom_queue.put(root.right_child)
    return root

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
                return 'Deep node deleted successfully'
            else:
                custom_queue.put(root.left_child)
        if root.right_child:
            if root.right_child == deep_node:
                root.right_child = None
                return 'Deep node deleted successfully'
            else:
                custom_queue.put(root.right_child)

def get_min_value(root_node):
    while root_node.left_child:
        root_node = root_node.left_child
    return root_node

def delete_node(root_node, value):
    if not root_node:
        return
    if value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child:
            return root_node.right_child
        elif root_node.right_child:
            return root_node.left_child
        min_node = get_min_value(root_node.right_child)
        root_node.data = min_node.data
        root_node.right_child = delete_node(root_node.right_child, min_node.data)
    return root_node

def pre_order_traverse(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traverse(root_node.left_child)
    pre_order_traverse(root_node.right_child)

binary_search_tree = BinarySearchTree(40)
insert_node(binary_search_tree, 20)
insert_node(binary_search_tree, 10)
insert_node(binary_search_tree, 30)
insert_node(binary_search_tree, 60)
insert_node(binary_search_tree, 50)
insert_node(binary_search_tree, 70)
pre_order_traverse(binary_search_tree)
print(search_value(binary_search_tree, 80))

