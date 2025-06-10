class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

    def __str__(self):
        result = ''
        current_node = self
        while current_node is not None:
            result += str(current_node.value)
            if current_node.next is not None:
                result += ' -> '
            current_node = current_node.next
        return result

def create_linkedlist_from_list(values):
    temp_node = current_node = Node()
    for value in values:
        current_node.next = Node(value)
        current_node = current_node.next
    return temp_node.next


# Leetcode - 206 : Reverse Linkedlist - Reverse element order in a linkedlist
def reverse_linkedlist(head):
    current_node = head
    prev_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node

def sort_linkedlist(head):
    temp_node = head
    current_node = head
    while current_node.next is not None:
        if current_node.value > current_node.next.value:
            temp_node.next = current_node.next
        else:
            temp_node.next = current_node
    return temp_node

# Leetcode - 143 : Merge linkedlist - Merge two linkedlist in an ascending order
def merge_linkedlist(l1, l2):
    ...

elements = [5, 2, 4, 1, 7, 3, 6]
linkedlist_1 = create_linkedlist_from_list(elements)
print(linkedlist_1)
print(reverse_linkedlist(linkedlist_1))
sorted_linkedlist = sort_linkedlist(linkedlist_1)
print(sorted_linkedlist)


