n,d=map(int,input().split())
lt=[]
ap={}
for _ in range(n):
    a,b,t=input().split()
    lt.append(sorted([a,b,t],reverse=True))
    if lt[_][0]+lt[_][1] not in ap:
        ap[lt[_][0]+lt[_][1]]=[int(t)]
    else:
        ap[lt[_][0]+lt[_][1]].append(int(t))
count=0
for value in ap.values():
    if len(value)<2:
        continue
    i=value[0]
    j=value[1]
    if abs(i-j)<=d:
        count+=1
print(count)
    

    