class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last_node = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        if self.last_node is not None:
            self.last_node.next = new_node
        self.last_node = new_node

    def reverse(self):
        predecessor, current, successor = None, self.head, None
        while current:
            successor = current.next
            current.next = predecessor
            predecessor = current
            current = successor
        self.head = predecessor

    def print(self):
        result = f'List: {str(self.head.value)}'
        current = self.head.next
        while current:
            result = result + '->' + str(current.value)
            current = current.next
        print(result)


if __name__ == '__main__':
    mylist = LinkedList()
    mylist.add_node(1)
    mylist.add_node(2)
    mylist.add_node(3)
    mylist.add_node(4)
    mylist.add_node(5)
    mylist.print()
    mylist.reverse()
    mylist.print()