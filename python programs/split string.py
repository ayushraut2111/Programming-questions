s=input()
a=s.split()
z=''
for i in range(len(a)):
    if(i==len(a)-1):
        z=z+a[i]
    else:
        z=z+a[i]+'-'

print(z)