#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    string s;
    cin>>s;
    int a[256];
    for(int i=0;i<256;i++)
    {
        a[i]=0;
    }
    for(auto x:s)
    {
        a[int(x)]++;
    }
    for(int i=0;i<256;i++)
    {
        if (a[i]!=0)
        {
            cout<<char(i)<<" "<<a[i]<<endl;
        }
    }
}