from statistics import mean

n,m=map(int,input().split())
a=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    s=list(map(int,input().split()))
    for j in range(m):
        a[i][j]=s[j]
x=list(list(x) for x in (zip(*a)))
l=[0 for i in range(n)]
count=0
for i in x:
    mi=max(i)
    for j in i:
        if j==mi:
           cp=i.index(j)
           x[count][cp]=-1
           l[cp]+=1
    count+=1
maxi=max(l)
for i  in range(len(l)):
    if l[i]==maxi:
        l[i]=mean(a[i])
print(l.index(max(l))+1)