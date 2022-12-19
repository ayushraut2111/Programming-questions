n= int(input())
a = list(map(int, input().split()))


nb = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        m = max(a[i:j + 1])
        if a[i] * a[j] <= m:
            nb += 1
print(nb)