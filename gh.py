n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(n-2):
    ans.append(a[i+1]+a[i+2])
ans.append(a[n-1]+a[0])
ans.append(a[0]+a[1])
print(ans)
