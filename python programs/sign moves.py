t=int(input())
for _ in range(t):
    n=int(input())
    total=(n*(n+1))//2
    if n%2==0:
       o=(n//2)
    else:
        o=(n//2)+1
    print(total-2*(o**2))