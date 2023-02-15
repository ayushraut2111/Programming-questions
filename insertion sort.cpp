#include<bits/stdc++.h>
#define ll long long
using namespace std;
void insertionsort(int a[],int n)
{
    for(int i=1;i<n;i++)
    {
        int temp=a[i];
        int j=i-1;
        while(j>=0&&temp<=a[j])
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=temp;
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
    insertionsort(a,n);
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<endl;
    }
}