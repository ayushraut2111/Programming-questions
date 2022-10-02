def mergeIntervals(intervals):
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    return stack
a ="aa"
b="a"
a=list(a)
b=list(b)
l={}
d={c:i for i,c in enumerate(a)}
for key,value in d.items():
    l[key]=[a.index(key),value]
# print(l)
ans={}
for i in b:
    if i in a:
        ans[i]=l[i]
if len(ans)==0:
    print(-1)
p=[]
for i in ans.values():
    p.append(i)
p.sort()
print(p)
if p[len(p)-1][0]-p[0][1]==1:
    print(1)
print(p[len(p)-1][0]-p[0][1]+1)
