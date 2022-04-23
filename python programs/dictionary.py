a={}
for i in range(3):
    b=[j for j in range(i)]
    a[i]=b
for key,value in a.items():
    for i in value:
        print (i)
    