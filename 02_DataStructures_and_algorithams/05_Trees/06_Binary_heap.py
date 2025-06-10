class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

def peek_of_heap(root_node):
    if not root_node:
        return root_node
    else:
        return root_node.custom_list[1]

def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size

def level_order_traverse(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i])

def heapify_tree_insert(root_node, index, heap_type):
    parent_index = int(index / 2)
    if index <= 1:
        return
    if heap_type == "min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)

def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "The binary heap is full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "The value is inserted successfully"

def heapify_tree_extract(root_node, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_index = 0
    if root_node.heap_size < left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == "min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
        elif heap_type == "max":
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
    else:
        if heap_type == "min":
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_index = left_index
            else:
                swap_index = right_index
            if root_node.custom_list[index] > root_node.left_child[swap_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_index]
                root_node.custom_list[swap_index] = temp
        elif heap_type == "max":
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_index = left_index
            else:
                swap_index = right_index
            if root_node.custom_list[index] < root_node.left_child[swap_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_index]
                root_node.custom_list[swap_index] = temp
    heapify_tree_extract(root_node, swap_index, heap_type)

def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        extracted_node = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_tree_extract(root_node, 1, heap_type)
        return extracted_node

def delete_heap(root_node):
    root_node.custom_list = None


min_heap = Heap(10)
insert_node(min_heap, 4, "min")
insert_node(min_heap, 18, "min")
insert_node(min_heap, 6, "min")
insert_node(min_heap, 8, "min")
insert_node(min_heap, 12, "min")
insert_node(min_heap, 10, "min")
insert_node(min_heap, 16, "min")
insert_node(min_heap, 14, "min")


level_order_traverse(min_heap)