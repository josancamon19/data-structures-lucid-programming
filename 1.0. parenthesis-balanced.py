from stack import Stack


def c_reversed(char):
    if char == '(':
        return ')'
    elif char == '{':
        return '}'
    elif char == '[':
        return ']'
    elif char == ')':
        return '('
    elif char == '}':
        return '{'
    elif char == ']':
        return '['


if __name__ == '__main__':
    stack = Stack()
    w = '{[()]}'
    for c in w:
        if stack.peek() is not None and stack.peek().data == c_reversed(c):
            # print(stack.peek().data, c)
            stack.pop()
        else:
            # print('inserting')
            stack.push(c)

    if stack.is_not_empty():
        print('Unbalanced string')
    else:
        print('Balanced String')
