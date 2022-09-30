for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    even,odd=0,0
    for num in a:
        if num % 2 == 0:
            even += 1
        else:
            odd+= 1
    if even==0 or odd==0:
        print("Alice")
    else:
        if even==odd:
            print("Alice")
        elif even>odd:
            print("Bob")
        else:
            print("Alice")