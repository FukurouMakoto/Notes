class linked_list_node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node #Pointer to next node

class linked_list:
    def __init__(self, head=None):
        self.head = head #establishes where the head is

    def insert(self, value): #Creates node for value, then adds it to the list
        node = linked_list_node(value) #creates node with value
        if self.head is None: 
            self.head = node #if list has no head, the current node is set to head
            return #Will only occur when list is empty

        current_node = self.head  #traverses the list and finds a node with no next node 
        while True: #and assings the current node to that node's next pointer.
            if current_node.next_node is None:
                current_node.next_node = node
                break
            current_node = current_node.next_node

    def print_linked_list(self): #Traverses and prints the list for testing purposes
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.value} '->'")
            current_node = current_node.next_node
        print("None")

ll = linked_list()
ll.print_linked_list()
ll.insert('3')
ll.print_linked_list()
ll.insert('44')
ll.print_linked_list()
ll.insert('55')
ll.print_linked_list()