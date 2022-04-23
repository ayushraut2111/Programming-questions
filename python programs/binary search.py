def binarysearch(a,key,first,last):
    if first<=last:
        mid=(first+last)//2
        if a[mid]==key:
            return True
        elif a[mid]<key:
            return binarysearch(a,key,mid,last)
        else:
           return binarysearch(a,key,first,mid)
    return False

if __name__=='__main__':
    print("enter the list")
    a=map(int,input().split())
    a=list(a)
    a.sort()
    print("enter the number you want to search")
    key=int(input())
    s=binarysearch(a,key,0,len(a))
    if s==True :
        print("found")
    else:
        print("not found")
