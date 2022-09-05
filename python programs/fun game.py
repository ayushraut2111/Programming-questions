n=int(input())
a=list(map(int,input().split()))
b=a[:]
ans=[]
a.reverse()
while len(a)>0 and len(b)>0:
    if a[len(a)-1]>b[len(b)-1]:
        ans.append(1)
        b.pop()
    elif a[len(a)-1]<b[len(b)-1]:
        ans.append(2)
        a.pop()
    else:
        ans.append(0)
        a.pop()
        b.pop()
for i in ans:
    print(i,end=" ")