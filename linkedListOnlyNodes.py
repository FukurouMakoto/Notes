class linked_list_node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


node1 = linked_list_node("3")
node2 = linked_list_node("7")
node3 = linked_list_node("10")        

node1.next_node = node2
node2.next_node = node3

current_node = node1
while True:
    print(f'{current_node.value} -> ')
    if current_node.next_node is None:
        print(f"None")
        break
    current_node = current_node.next_node