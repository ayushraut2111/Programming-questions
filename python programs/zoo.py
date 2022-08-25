a=input()
x=0
y=0
if a[0]!='z':
    print("NO")
    pass
for i in a:
    if i=='z':
        x+=1
    else:
        y+=1

if 2*x==y:
    print("YES")
else:
    print("NO")


# a=[1,2]
# b=[3,4]
# l=a+b
# print(l)