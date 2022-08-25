n,q=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    x=a[0:l-1]+a[r:n]
    print(max(x))