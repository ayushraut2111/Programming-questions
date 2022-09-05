from collections import deque as q
a=q([1,2,3,4])
a.append(5)
print(type(a),a)
x=a.popleft()
print(x,list(a))