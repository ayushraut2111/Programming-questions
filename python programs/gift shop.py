t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=map(int,input().split())
    a=list(a)
    a.sort()
    count=0
    for j in a:
        if j<k:
            count+=1
            k-=j
        elif (j/2)<=k:
            count+=1
            k-=(j/2)
        else:
            break
    print(count)
    