# linked list from the programmer in you channel
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_head(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp_head = self.head
            self.head = new_node
            new_node.next = temp_head
            del temp_head

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_position(self, new_node, position):
        if position < 1:
            self.insert_head(new_node)
            return

        current = self.head
        counter = 0
        while current.next is not None:
            if counter + 1 == position:
                new_node.next = current.next
                current.next = new_node
                break
            counter += 1
            current = current.next

        if position > counter:
            print('Position', position, 'not available, inserting at position', counter)
            current.next = new_node

    def delete_end(self):
        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            if current.next.next is None:
                print('---- deleting last node ---- ->', current.next.data)
                current.next = None
                break
            current = current.next

    def delete_head(self):
        if self.head is None:
            return
        print('deleting head -->', self.head.data)
        self.head = self.head.next

    def delete_at_position(self, position):
        if self.head is None:
            return

        if position == 0:
            self.delete_head()
            return

        current = self.head
        counter = 0

        while current.next is not None:
            if counter + 1 == position:
                print('deleting at position  -->', position, current.next.data)
                if current.next.next is not None:
                    current.next = current.next.next
                else:
                    current.next = None
                break

            counter += 1
            current = current.next

    def print_list(self):
        if self.head is None:
            print('Head is empty')
        current = self.head
        print(current.data)
        while current.next is not None:
            print(current.next.data)
            current = current.next


if __name__ == '__main__':
    # Node -> data, next
    first_node = Node('Joan')
    linked_list = LinkedList()
    linked_list.insert_end(first_node)

    second_node = Node('Santiago')
    linked_list.insert_end(second_node)

    third_node = Node('Cabezas')
    linked_list.insert_end(third_node)

    fourth_node = Node('Monroy')
    linked_list.insert_at_position(fourth_node, 1)

    linked_list.print_list()
    # linked_list.delete_end()
    print('\n')
    linked_list.delete_head()
    linked_list.delete_at_position(1)
    linked_list.print_list()
