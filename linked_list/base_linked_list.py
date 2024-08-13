class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Singly_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    
    def create_linked_list(self, arr):
        self.size = len(arr)
        for i in arr:
            node = Node(i)
            if self.head == None:
                self.head = self.tail = current_node = node
            else:
                current_node.next = node
                current_node = self.tail = node

    
    def print_linked_list(self):
        current_node = self.head
        while True:
            if current_node is None:
                break
            else:
                print(current_node.value)
                current_node = current_node.next


s = Singly_Linked_List()
s.create_linked_list([1,2,3,4])
s.print_linked_list()
