t=int(input())
for _ in range(t):
    n=int(input())
    a=1
    b=1
    x=0
    for i in range(2,n+1):
        a=a|i
        if a==b:
            x+=1
        b=a
    print(x)