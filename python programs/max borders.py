for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        h=input()
        for j in range(m):
            a[i][j]=h[j]
    
    # for i in range(n):
    #     for j in range(m):
    #         print(a[i][j],end=" ")

    g=0

    for i in range(n):
        count=0
        for j in range(m):
            if a[i][j]!='#':
                g=max(g,count)
                count=0
            else:
                count+=1
                g=max(g,count)
    for j in range(m):
        count=0
        for i in range(n):
            if a[i][j]!='#':
                g=max(g,count)
                count=0
            else:
                count+=1
                g=max(g,count)
    print(g)
