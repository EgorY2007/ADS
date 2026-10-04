def f(a,b,c,d,x):
    return a*x**3 + b*x**2 + c*x + d

a,b,c,d = map(int, input().split())

l = -10000
r = 10000
while r - l > 1e-5:
    m = (r + l) / 2
    if f(a,b,c,d,l) * f(a,b,c,d,m) > 0:
        l = m
    else:
        r = m
print(m)
