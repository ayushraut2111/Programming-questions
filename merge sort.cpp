#include<bits/stdc++.h>
#define ll long long
using namespace std;
void merge(int a[],int beg,int mid,int end)
{
    int n1=mid-beg+1;
    int n2=end-mid;
    int left[n1];
    int right[n2];
    for(int i=0;i<n1;i++)
    {
        left[i]=a[beg+i];
    }
    for(int i=0;i<n2;i++)
    {
        right[i]=a[mid+i+1];
    }
    int i=0,j=0,k=beg;
    while(i<n1&&j<n2)
    {
        if(left[i]<right[j])
        {
            a[k]=left[i];
            i++;
            k++;
        }
        else{
            a[k]=right[j];
            j++;
            k++;
        }
    }
    while(i<n1)
    {
        a[k]=left[i];
        i++;k++;
    }
    while(j<n2)
    {
        a[k]=right[j];
        k++;j++;
    }
    
}
void mergesort(int a[],int beg,int end)
{
    if(beg<end)
    {
        int mid=(end+beg-1)/2;
        mergesort(a,beg,mid);
        mergesort(a,mid+1,end);
        merge(a,beg,mid,end);
    }
}
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    mergesort(a,0,n);
}