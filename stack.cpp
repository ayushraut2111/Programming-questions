#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    string s;
    cin>>s;
    int r;
    cin>>r;
    stack<char>stc;
    for(int i=0;i<s.length();i++)
    {
        if(stc.empty()||s[i]!=stc.top())
        stc.push(s[i]);
        else
        stc.pop();
    }
    string a;
    while(!stc.empty())
    {
        a+=stc.top();
        stc.pop();
    }
    cout<<a<<endl;
}