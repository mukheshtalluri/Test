from queue import Queue

class AVLTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

def pre_order_traverse(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traverse(root_node.left_child)
    pre_order_traverse(root_node.right_child)

def search_value(root_node, value):
    if not root_node:
        return 'Value not found'
    if root_node.data == value:
        return 'Value found'
    elif value < root_node.data:
        return search_value(root_node.left_child, value)
    else:
        return search_value(root_node.right_child, value)

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def left_rotate(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = new_root.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def right_rotate(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = new_root.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert_node(root_node, value):
    if not root_node:
        return AVLTree(value)
    elif value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, value)
    else:
        root_node.right_child = insert_node(root_node.right_child, value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    # Left Left
    if balance > 1 and value < root_node.left_child.data:
        return right_rotate(root_node)
    # Left Right
    if balance > 1 and value > root_node.left_child.data:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    # Right Right
    if balance < -1 and value > root_node.right_child.data:
        return left_rotate(root_node)
    # Right Left
    if balance < -1 and value < root_node.right_child.data:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)

    return root_node

def min_value(root_node):
    current = root_node
    while current.left_child:
        current = current.left_child
    return current

def delete_node(root_node, value):
    if not root_node:
        return root_node
    elif value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        # Node with one child or no child
        if not root_node.left_child:
            return root_node.right_child
        elif not root_node.right_child:
            return root_node.left_child
        # Node with two children
        min_node = min_value(root_node.right_child)
        root_node.data = min_node.data
        root_node.right_child = delete_node(root_node.right_child, min_node.data)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    # Rebalancing
    if balance > 1 and get_balance(root_node.left_child) >= 0:
        return right_rotate(root_node)
    if balance > 1 and get_balance(root_node.left_child) < 0:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) <= 0:
        return left_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) > 0:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)

    return root_node

def delete_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return 'AVL Tree is deleted successfully.'

avl_tree = AVLTree(10)
avl_tree = insert_node(avl_tree, 20)
avl_tree = insert_node(avl_tree, 30)
avl_tree = insert_node(avl_tree, 40)
avl_tree = insert_node(avl_tree, 50)
avl_tree = insert_node(avl_tree, 60)
avl_tree = insert_node(avl_tree, 70)
pre_order_traverse(avl_tree)
