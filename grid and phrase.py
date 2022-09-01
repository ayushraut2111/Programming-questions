n,m=map(int,input().split())
a=[]
for i in range(n):
    s=input()[:m]
    a.append(s)

count=0
for i in a:
    if "saba" in i:
        count+=1
for i in range(m):
    s=''
    for j in range(n):
        s+=a[j][i]
    if "saba" in s:
        count+=1
s=''
for i in range(min(n,m)):
    s+=a[i][i]
if "saba" in s:
    count+=1
s=''
for i in range(min(n,m))[::-1]:
    s+=a[i][m-i-1]
if "saba" in s:
    count+=1
print(count)