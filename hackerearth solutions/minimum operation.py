n=int(input())
a=list(map(int,input().split()))
if len(a)==1:
    print(1)
else:
    count=1
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            count+=1
    print(count)