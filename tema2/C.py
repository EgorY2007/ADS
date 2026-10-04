def f(x):
    return x**2 + x**(1/2)

c = float(input())

l = 0
r = 10**9
for i in range(100):
    m = (l + r) / 2
    if f(m) < c:
        l = m
    else:
        r = m
print(f"{m:.6f}")
