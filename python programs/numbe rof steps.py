def ans(n,a,b):
    m=min(a)
    count=0
    for i in range(n):
        if a[i]>m:
            while a[i]>m:
                a[i]-=b[i]
                count+=1
            if a[i]!=m:
                return -1
        else:
            continue
    return count

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(ans(n,a[:],b[:]))

