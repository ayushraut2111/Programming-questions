a=[i for i in range(1,int(10e6+1))]
b=sum(a)
for _ in range(int(input())):
    l,r=map(int,input().split())
    for i in range(l-1,r):
        a[i]=0
x=b-sum(a)
print(x)
