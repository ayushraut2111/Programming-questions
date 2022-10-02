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

s1 = "cocoplaydae"
s=list(s1)
l=[]
d={c:i for i,c in enumerate(s)}
for key,value in d.items():
    l.append([s.index(key),value])
stack=mergeIntervals(l)
ans=[]
for i in stack:
    ans.append(i[1]-i[0]+1)
print(ans)
# print(stack)
