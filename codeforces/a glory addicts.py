def solve(l0,l1,diff):
    ans=0
    i=min(l0,l1)
    while i:
        ans+=2*l0[i]
        ans+=2*l1[i]
    return ans
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:n]
    z=a.count(0)
    o=a.count(1)
    l=list(zip(a,b))
    l.sort()
    l0=l[:z]
    l1=l[z:]
    l0.sort(reverse=True)
    l1.sort(reverse=True)
    diff=abs(z-o)
    maxl0,maxl1=max(l0)[1],max(l1)[1]
    print(maxl0,maxl1)
    if maxl0>=maxl1:
        print(solve(l0[:],l1[:],diff-1))
    else:
        print(solve(l1[:],l0[:],diff-1))

    
