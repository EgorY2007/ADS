n = input().split()

stack = []

for s in n:
    if s in '+-*':
        b = stack.pop()
        a = stack.pop()
        if s == '+':
            otv = a + b
        if s == '-':
            otv = a - b
        if s == '*':
            otv = a * b
        stack.append(otv)
    else:
        stack.append(int(s))
print(stack[0])
