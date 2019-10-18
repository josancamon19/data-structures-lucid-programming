from stack import Stack

if __name__ == '__main__':
    num = 19
    stack = Stack()
    while num != 0:
        stack.push(str(num % 2))
        num //= 2

    binary = ''
    while stack.is_not_empty():
        binary += stack.pop()
        
    print(binary, int(binary, 2))
