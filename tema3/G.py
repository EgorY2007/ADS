n = int(input())
a = list(map(int, input().split()))

stack = []
need = 1

for x in a:
    stack.append(x)
    while stack and stack[-1] == need:
        stack.pop()
        need += 1

if need == n + 1:
    print('YES')
else:
    print('NO')
