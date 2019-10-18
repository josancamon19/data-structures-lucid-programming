from stack import Stack

if __name__ == '__main__':
    string = 'abcd'
    stack = Stack()
    for c in string:
        stack.push(c)

    reversed_s = ''
    while stack.is_not_empty():
        reversed_s += stack.pop()

    print(reversed_s)