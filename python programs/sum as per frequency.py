n=int(input())
a=list(map(int,input().split()))
for _ in range(int(input())):
    l,r=map(int,input().split())
    mp={}
    for i in a:
        if i in mp:
            mp[i]+=1
        else:
            mp[i]=1
    ans=0
    for i,j in mp.items():
        if j>=l and j<=r:
            ans+=(i*j)
    print(ans)

