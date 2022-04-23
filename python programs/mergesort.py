def merge(a,beg,mid,end):
    l1=mid-beg+1
    l2=end-mid
    h1=a[beg:mid+1]
    h2=a[mid+1:end]
    i=0
    j=0
    k=beg
    while i<l1 and j<l2:
        if h1[i]<h2[j]:
            a[k]=h1[i]
            i=i+1
        else:
            a[k]=h2[j]
            j=j+1
        k=k+1
    while i<l1:
        a[k]=h1[i]
        i=i+1
        k=k+1
    while j<l2:
        a[k]=h2[j]
        j=j+1
        k=k+1
   

def mergesort(a,beg,end):
    if beg<=end:
        mid=len(a)//2
        mergesort(a,beg,mid-1)
        mergesort(a,mid,end)
        merge(a,beg,mid,end)

a=[1,21,3,6]
mergesort(a,0,len(a))
print(a)