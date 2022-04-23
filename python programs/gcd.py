def gcd(a,b):
    if a%2==0:
        if b-a>=2:
            print(str(a)+" "+str(a+2))
            return
        else:
            print(-1)
            return
    elif b-a>2:
        if a%3==0:
            print(str(a)+" "+str(a+3))
            return 
        else:
            print(str(a+1)+" "+str(a+3))
            return

    print(-1)
    return 

for _ in range(int(input())):
    a,b=map(int,input().split())
    gcd(a,b)