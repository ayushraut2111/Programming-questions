t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    a=sorted(s)
    print(a)
    c0=a.count('0')
    c1=a.count('1')
    if c0==0 or c1==0:
        print(1)
    elif c0==c1:
        print(2*c0)
    else:
        print(2*min(c0,c1)+1)