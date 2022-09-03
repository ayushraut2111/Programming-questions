#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    int n,k;
    cin>>n>>k;
    int a[n];
    for(int i=0;i<n;i++)
    cin>>a[i];
    priority_queue<int>pq;
    for(int i=0;i<=k;i++)
    {
        pq.push(a[i]);
    }
    for(int i=k+1;i<n;i++)
    {
        if(a[i]>pq.top())
        {
            pq.pop();
            pq.push(a[i]);
        }
    }
    int ans=0;
    while(!pq.empty())
    {
        ans=pq.top();
        pq.pop();
    }
    cout<<ans<<endl;
}