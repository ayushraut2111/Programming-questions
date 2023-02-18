#include<bits/stdc++.h>
#define ll long long
using namespace std;
int quick(int a[],int beg,int end)
{
    int pivot=a[end-1];
    int i=beg-1;
    for(int j=beg;j<end-1;j++)
    {
        if(a[j]<=pivot)
        {
            i++;
            swap(a[i],a[j]);
        }   
    }
    swap(a[i+1],a[end-1]);
    return i+1;
}
void quicksort(int a[],int beg,int end)
{
    if(beg<end)
    {
        int pi=quick(a,beg,end);
        quicksort(a,beg,pi-1);
        quicksort(a,pi+1,end);
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
    quicksort(a,0,n);
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<endl;
    }
}