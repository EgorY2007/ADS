class Deque:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0

    def push_front(self, item):
        self.items = [item] + self.items
        return 'ok'
    
    def push_back(self, item):
        self.items.append(item)
        return 'ok'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)
    
    def pop_back(self):
        if self.is_empty():
            return 'error'
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def back(self):
        if self.is_empty():
            return 'error'
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return 'ok'

deq = Deque()
while True:
    command = input().split()
    cmd = command[0]
    
    if cmd == 'push_front':
        print(deq.push_front(int(command[1])))
    elif cmd == 'push_back':
        print(deq.push_back(int(command[1])))
    elif cmd == 'pop_front':
        print(deq.pop_front())
    elif cmd == 'pop_back':
        print(deq.pop_back())
    elif cmd == 'front':
        print(deq.front())
    elif cmd == 'back':
        print(deq.back())
    elif cmd == 'size':
        print(deq.size())
    elif cmd == 'clear':
        print(deq.clear())
    elif cmd == 'exit':
        print('bye')
        break
