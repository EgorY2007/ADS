s = input()
stack = []
otv = True

for c in s:
    if c in ['(','{','[']:
        stack.append(c)
        continue
    if len(stack) != 0 and (c == ')' and stack[-1] == '(' or
                            c == ']' and stack[-1] == '[' or
                            c == '}' and stack[-1] == '{'):
        stack.pop()
    else:
        otv = False
        break
    
if len(stack) != 0:
    otv = False
if otv:
    print('yes')
else:
    print('no')
