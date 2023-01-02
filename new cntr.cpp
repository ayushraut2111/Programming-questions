#include<bits/stdc++.h>
#define ll long long
using namespace std;
void newcontr(int *arr,int n)
{
    int x=arr[0];
    int y=arr[1];
    for(int i=0;i<n-2;i++)
    {
        arr[i]=arr[i+1]+arr[i+2];
    }
    arr[n-2]=arr[n-1]+x;
    arr[n-1]=x+y;
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    cin>>arr[i];
    newcontr(arr,n);
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<endl;
    }
}