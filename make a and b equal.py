for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count1=0
    count2=0
    for i in range(n):
        if a[i]>b[i]:
            count1+=abs(a[i]-b[i])
        else:
            count2+=abs(a[i]-b[i])
    if count1==count2:
        print(count1)
    else:
        print(-1)