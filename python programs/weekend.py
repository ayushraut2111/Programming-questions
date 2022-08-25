t=int(input())
for j in range(t):
    n=int(input())
    if n<6:
        print(0)
    elif n==6:
        print(1)
    else:
        n-=6
        print((n//7)+1)