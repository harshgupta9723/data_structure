#node creation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    l_list = linked_list()
    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)


    l_list.head.next = second
    second.next = third
    third.next = fourth

    l_list.printlist()