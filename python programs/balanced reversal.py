t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    s=list(s)
    s.sort()
    d=''
    for i in s:
        d+=str(i)
    print(d)