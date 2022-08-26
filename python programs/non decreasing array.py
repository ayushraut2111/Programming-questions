for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[a[0]]
    for i in range(1,len(a)):
        if a[i]>=b[i-1]:
            b.append(a[i])
        else:
            if b[i-1]%a[i]==0:
                b.append(b[i-1])
                continue
            x=a[i]+b[i-1]
            x=x//a[i]
            b.append(a[i]*x)
    for i in b:
        print(i,end=" ")
    print()
