s='alison 12heck'
a=s.split()
z=''
for i in range(len(a)):
        if i==len(a)-1:
          z+=a[i][0].upper()+a[i][1:]
        else:
            z+=a[i][0].upper()+a[i][1:]+' '
print(z)
            
            