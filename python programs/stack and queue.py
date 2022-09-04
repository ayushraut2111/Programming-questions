n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
x=0
# if sum(a[0:k])>sum(a[n-k-1:]):
#     ans=sum(a[:k])
# else:
#     ans=sum(a[n-1-k:])
for i in range(n):
    x=i
    if a[i]>a[n-1] and k>0:
        ans+=a[i]
        k-=1
    else:
        break
if sum(a[x:x+k])<sum(a[n-x-1:n]):
    for i in range(x,n)[::-1]:
        if k!=0:
            ans+=a[i]
            k-=1
        else:
            break
else:
    for i in range(x,x+k):
        ans+=a[i]
print(ans)
