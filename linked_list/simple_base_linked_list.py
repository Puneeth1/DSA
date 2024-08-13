class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


def print_linked_list():
    current_node = head
    while True:
        if current_node is None:
            break
        else:
            print(current_node.value, end=' ')
            current_node = current_node.next
    print()

print_linked_list()
