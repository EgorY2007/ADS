from collections import deque

def balance():
    if len(left) > len(right) + 1:
        right.appendleft(left.pop())
    elif len(left) < len(right):
        left.append(right.popleft())

n = int(input())

left = deque()
right = deque()
otv = []

for _ in range(n):
    line = input()
    op = line[0]

    if op == '+':
        right.append(int(line[2:]))
        balance()
    elif op == '*':
        i = int(line[2:])
        if len(left) == len(right):
            right.appendleft(i)
        else:
            left.append(i)
        balance()
    else:
        otv.append(str(left.popleft()))
        balance()

print('\n'.join(otv))
