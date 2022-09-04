def solve(n,m,a,s):
    for i in range(len(s)):
        if s[i] in a[i%n]:
            a[i%n][a[i%n].index(s[i])]='#'
        else:
            return False
    return True

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        s=list(input()[:m])
        a.append(s)
    s=input()
    if solve(n,m,a,s):
        print("Yes")
    else:
        print("No")
