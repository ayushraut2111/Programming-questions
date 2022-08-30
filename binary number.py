from posixpath import split


def ans(x):
    a=0
    n=1
    while(x):
        p=n
        while(p):
            if p & 3==3:
                break
            p=p>>1
        if p==0:
            a=n
            x-=1
        n+=1
    return a
for _ in range(int(input())):
    k=int(input())
    print(int(bin(ans(k)).split('0b')[1]))
