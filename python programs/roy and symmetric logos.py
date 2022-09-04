def solve(n,a):
    for i in range(n):
        for j in range((n//2)+1):
            if a[i][j]!=a[i][n-1-j]:
                return False
    for i in range((n//2)+1):
        for j in range(n):
            if a[i][j]!=a[n-1-i][j]:
                return False
    return True
            
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        s=list(input())
        a.append(s)
    if solve(n,a[:]):
        print("YES")
    else:
        print("NO")
