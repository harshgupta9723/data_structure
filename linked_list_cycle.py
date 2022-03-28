class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        
        new_node.next = self.head
        
        self.head = new_node
        
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

        
linked_list = LinkedList()

linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)

linked_list.print_list()

# why linked list print in reverse order.