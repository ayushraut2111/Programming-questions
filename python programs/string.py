t=int(input())
for y in range(t):
    a=input()
    b=input()
    c=''
    for i in range(len(a)):
        if a[i]==b[i]:
            c+='g'
        else:
            c+='b'
    print(c)
