for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    ans=[]
    for i in range(q):
        count=0
        if r[i]-l[i]<=n:
            for j in range(l[i],r[i]+1):
                count+=a[(j-1)%n]
            ans.append(count)
        else:
            p=0
            for j in range(l[i],r[i]+1):
                if (j-1)%n!=0:
                    count+=a[(j-1)%n]
                    p+=1
                else:
                    break
            c=r[i]-l[i]+1-p
            if c<n:
                for j in range(c):
                    count+=a[j]
            else:
                x=c//n
                count+=sum(a)*x
                c-=len(a)*x
                for j in range(c):
                    count+=a[j]
            ans.append(count)

    for i in ans:
        print(i,end=" ")
    print()
    