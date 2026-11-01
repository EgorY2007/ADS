class Heap:
    def __init__(self):
        self.heap = [None]
        self.size = 0
        
    def shift_up(self,i):
        while i//2 > 0 and self.heap[i] > self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2
            
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shift_up(self.size)

    def shift_down(self,i):
        while i * 2 <= self.size:
            j = self.ind_max_child(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
            i = j

    def ind_max_child(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def del_max(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.shift_down(1)
        return removed

heap = Heap()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == '0':
        k = int(command[1])
        heap.insert(k)
    else:
        print(heap.del_max())
        














        
        
