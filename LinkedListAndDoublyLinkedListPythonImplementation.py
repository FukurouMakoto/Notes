class node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def return_data(self):
        return self.data
    
    def get_next_node(self):
        if self.next_node == None:
            return None
        return self.next_node.data
    
    def get_previous_node(self):
        if self.prev_node == None:
            return None
        return self.prev_node.data

class doubly_linked_list:
    def __init__(self, size=0, head=None, tail=None):
        self.size = size
        self.head = head
        self.tail = tail 

    #return the size of the linked list
    def size(self):
        return self.size
    
    #get head node for testing purposes
    def get_head(self):
        return self.head.data

    #get tail node for testing purposes
    def get_tail(self):
        return self.tail.data

    #Is this linked list empty?
    def is_empty(self):
        return self.size() == 0
    
    #Add item to linked list
    def add(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev_node = None
            return 
        
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = new_node
                current_node.prev_node = current_node
                self.tail = current_node.next_node
                break
            current_node = current_node.next_node


    def print_linked_list(self): #Traverses and prints the list for testing purposes
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}, next: {current_node.get_next_node()}, prev: {current_node.get_previous_node()}, head: {self.get_head()}, tail: {self.get_tail()} '->'")
            current_node = current_node.next_node
        print("None")
        
ll = doubly_linked_list()
ll.add('3')
ll.add('5')
ll.add('7')
ll.add('9')
ll.print_linked_list()