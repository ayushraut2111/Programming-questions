s = "xtrujidaujwmkkxod"
k = 25
s=list(s)
mp={}
for i in s:
    if i not in mp:
        mp[i]=1
    else:
        mp[i]+=1
l=[]
for key,value in mp.items():
    l.append(value)
l.sort()
count=0
if len(l)<k:
    print(0)
for i in range(len(l)-k):
    count+=l[i]
print(count)
