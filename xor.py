for _ in range(int(input())):
    t=input()
    a=list(map(int,input().split()))
    a.sort()
    x=a[0]
    ans=100000000
    for i in a[1:]:
        tmp=(x&i)^(x|i)
        x=i
        ans=min(ans,tmp)
    print(ans)