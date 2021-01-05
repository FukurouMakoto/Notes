class node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def return_data(self)
        return self.data
    
    def get_next_node(self):
        return self.next_node
    
    def get_previous_node(self):
        return self.prev_node

class doubly_linked_list:
    def __init__(self, size=0, head=None, tail=None):
        self.size = size
        self.head = head
        self.tail = tail 

    #return the size of the linked list
    def size(self):
        return self.size
    
    #Is this linked list empty?
    def is_empty(self):
        return self.size() == 0
    
    #Add item to linked list
    def add(self, data):
        node = node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        
        current_node = self.head
        previous_node - self.tail
        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                current_node.prev_node = None
                break
            current_node = current_node.next_node


        
        