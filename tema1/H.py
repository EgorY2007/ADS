class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dot_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n - 1):
            d1 = arr[j].x ** 2 + arr[j].y ** 2
            d2 = arr[j + 1].x ** 2 + arr[j + 1].y ** 2
            if d1 > d2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
                
n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(Point(x, y))

dot_sort(a)

for i in range(len(a)):
    print(a[i].x, a[i].y)
