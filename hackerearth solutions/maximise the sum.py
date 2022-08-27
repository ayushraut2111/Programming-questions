for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    mp={}
    for i in a:
        if i not in mp:
            mp[i]=1
        else:
            mp[i]+=1
    l=[]
    for i in mp:
        l.append(i*mp[i])
    l.sort(reverse=True)
    ans=0
    for i in l:
        p=ans
        ans=max(ans,ans+i)
        k-=1
        if k==0 or p==ans:
            print(ans)
            break
