class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)
        return 'ok'

    def pop(self):
        if self.is_empty():
            return 'error'
        return self.items.pop()

    def back(self):
        if self.is_empty():
            return 'error'
        return self.items[-1]
        
    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

stack = Stack()
while True:
    command = input().split()

    cmd = command[0]
    if cmd == 'push':
        print(stack.push(int(command[1])))
    elif cmd == 'pop':
        print(stack.pop())
    elif cmd == 'back':
        print(stack.back())
    elif cmd == 'size':
        print(stack.size())
    elif cmd == 'clear':
        print(stack.clear())
    elif cmd == 'exit':
        print('bye')
        break

