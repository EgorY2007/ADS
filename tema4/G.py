import heapq

n = int(input())
size = []
for _ in range(n):
    size.append(int(input()))

heap = []
for i in range(n):
    time_birth = max(1000 - size[i], 1)
    heapq.heappush(heap, (time_birth, i))

pos = 0
time = 0
otv = 0

while heap:
    t, i = heapq.heappop(heap)
    dist = abs(pos - i)
    if time + dist > t:
        otv = t
        break
    time = t
    pos = i
    size[i] += 1
    next_t = t + max(1000 - size[i], 1)
    heapq.heappush(heap, (next_t, i))

print(otv)
