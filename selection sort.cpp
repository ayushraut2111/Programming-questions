#include<bits/stdc++.h>
#define ll long long
using namespace std;
void selectionsort(int a[],int n)
{
    for(int i=0;i<n-1;i++)
    {
        int small=i;
        for(int j=i+1;j<n;j++)
        {
            if(a[j]<a[small])
            {
                small=j;
            }
        }
        int x=a[i];
        a[i]=a[small];
        a[small]=x;

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
    selectionsort(a,n);
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<endl;
    }
}