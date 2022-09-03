n,k=map(int,input().split())
a=list(map(int,input().split()))
pq=a[:k+1]
ans=100000000
ans=min(ans,max(pq))
for i in range(k+1,n):
    pq.sort()
    del pq[0]
    pq.append(a[i])
    ans=min(ans,max(pq))
print(ans)