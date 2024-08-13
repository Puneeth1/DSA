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
                print(current_node.value, end=' ')
                current_node = current_node.next
        print()
    
    def reverse_linked_list(self):
    # Initialise the three pointers
        prev = None
        curr = self.head
        next = curr.next

        while curr is not None:
            # move next by one step
            next = curr.next
            # create a link
            curr.next = prev

            # move the prev, curr by one step
            prev = curr
            curr = next

        # set a last element as new head
        self.head = prev


s = Singly_Linked_List()
s.create_linked_list([1,2,3,4])
s.reverse_linked_list()
s.print_linked_list()