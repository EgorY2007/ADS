dist = list(map(int, input().split()))
tarif = list(map(int, input().split()))

dist.sort()
tarif.sort(reverse=True)

otv = 0
for i in range(len(dist)):
    otv += dist[i] * tarif[i]

print(otv)
