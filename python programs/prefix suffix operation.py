t=int(input())
for g in range(t):
    n=int(input())
    a=map(int,input().split())
    b=map(int,input().split())
    a=list(a)
    b=list(b)
    c=[0]*n
    for i in range(n):
        c[i]=b[i]-a[i]
    s=c[:]
    s.sort()
    if s[0]<0:
        print(-1)
    else:
        for i in range(n):
            j=i+1
            if(c[i]!=c[j]):
                x=c[:i+1]
                y=c[i+1:]
                break
        while y[0]==0:
            del y[0]
        x1=x[:]
        y1=y[:]
        x1.sort()
        y1.sort()
        if(x1[0]!=x1[-1]) or (y1[0]!=y1[-1]):
            print(-1)
        else:
            print(x[0]+y[0])

