n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

for i in a2:
    l = -1
    r = len(a1)
    while r - l > 1:
        m = (l + r) // 2
        if a1[m] < i:
            l = m
        else:
            r = m
    if r == len(a1) or a1[r] != i:
        print('NO')
    else:
        print('YES')
    
        
