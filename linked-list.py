class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, new_data, position):
        new_node = Node(new_data)

        if position == 0:
            self.prepend(new_data)
            return

        current = self.head
        counter = 0
        while current.next is not None:
            if counter + 1 == position:
                new_node.next = current.next.next
                current.next = new_node
                break
            counter += 1
            current = current.next

    def print_items(self):
        if self.head is None:
            return
        current = self.head
        print(current.data)
        while current.next is not None:
            print(current.next.data)
            current = current.next


if __name__ == '__main__':
    linked_list = LinkedList()
    node0 = Node(data=0)
    node1 = Node(data=1)
    node2 = Node(data=2)

    linked_list.append(node1)
    linked_list.append(node2)
    # linked_list.print_items()
    linked_list.prepend(node0)
    linked_list.print_items()
