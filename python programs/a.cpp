#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
   int n,m;
   cin>>n>>m;
   vector<int>v1(n),v2(m);
   for(auto &x:v1)cin>>x;
   for(auto &x:v2)cin>>x;
   if(n==m==1)
   {
    if(v1[0]==v2[0])
    {
        cout<<"Banta"<<endl;
    }
    else
    cout<<"Alice"<<endl;
   }
   else
   cout<<"Alice"<<endl;
}