if __name__=='__main__':
    s=input()
    a=''
    for i in s:
        if(i==i.upper()):
            a+=i.lower()
        else:
            a+=i.upper()
    print(a)