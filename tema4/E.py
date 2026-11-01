import heapq

n = int(input())
a = list(map(int, input().split()))

heapq.heapify(a)

cost = 0
while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    cost = cost + ((x + y) * 0.05)
    heapq.heappush(a, x + y)

print(f"{cost:.2f}")
