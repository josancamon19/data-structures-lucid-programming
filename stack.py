class Node:
    def __init__(self, data):
        self.data = data
        self.bottomNode = None


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data)

        new_node.bottomNode = self.top
        self.top = new_node

    def pop(self):

        if self.top is None:
            return None
        elif self.top.bottomNode is not None:
            top = self.top.data
            self.top = self.top.bottomNode
            return top
        else:
            top = self.top.data
            self.top = None
            return top

    def get_stack(self):
        if self.top is None:
            return []

        items = []
        top = self.top

        while top.bottomNode is not None:
            items.append(top)
            top = top.bottomNode

        return items

    def is_empty(self):
        return self.top is None

    def is_not_empty(self):
        return self.top is not None

# if __name__ == '__main__':
#
#     node1 = Node(1)
#
#     node2 = Node(2)
#     node2.bottomNode = node1
#
#     stack = Stack()
#     stack.push(node1)
#     stack.push(node2)
#
#     print(stack.get_stack())
