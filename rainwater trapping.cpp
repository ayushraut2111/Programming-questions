#include<bits/stdc++.h>
using namespace std;
int rainwater(int a[],int n)
{
    vector<int>left(n),right(n);
    left[0]=a[0];
    right[n-1]=a[n-1];
    for(int i=1;i<n;i++)
    {
        left[i]=max(a[i],left[i-1]);
    }
    for(int i=n-2;i>=0;i--)
    {
        right[i]=max(a[i],right[i+1]);
    }
    int ans=0;
    for(int i=1;i<n-1;i++)
    {
        ans+=min(left[i],right[i])-a[i];
    }
    return ans;
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
    cout<<rainwater(a,n);
}