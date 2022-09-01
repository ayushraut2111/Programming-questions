n,q=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(q):
    y,z,d=input().split()
    y=int(y)
    z=int(z)
    if z not in a:
        print(-1)
    else:
        if d=='R':
            idx=y
            while a[idx]!=z:
                idx=(idx+1)%n
            count=0
            # while y!=idx:
            #     y=(y+1)%n
            #     count+=1
            if idx>=y:
                count+=(idx-y)
            else:
                count+=(n-1-y)
                count+=(idx+1)
            print(count)
        else:
            idx=y
            while a[idx]!=z:
                idx=(idx-1+n)%n
            count=0
            # while y!=idx:
            #     y=(y-1+n)%n
            #     count+=1
            if idx<=y:
                count+=y-idx
            else:
                count+=y
                count+=(n-idx)
            print(count)
