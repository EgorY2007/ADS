class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, n):
        self.items.append(n)
        return 'ok'

    def pop(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

que = Queue()
while True:
    command = input().split()
    cmd = command[0]
    
    if cmd == 'push':
        print(que.push(int(command[1])))
    elif cmd == 'pop':
        print(que.pop())
    elif cmd == 'front':
        print(que.front())
    elif cmd == 'size':
        print(que.size())
    elif cmd == 'clear':
        print(que.clear())
    elif cmd == 'exit':
        print('bye')
        break
