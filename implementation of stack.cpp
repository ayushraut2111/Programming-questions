#include<bits/stdc++.h>
#define ll long long
using namespace std;
struct mystack{
    int* arr;
    int cap,top;
    mystack(int x)
    {
        cap=x;
        top=-1;
        arr=new int[cap];
    }
    void push(int x)
    {
        if (top==cap-1)
        {
            cout<<"size is full"<<endl;
            return ;
        }
        top++;
        arr[top]=x;
    }
    int pop()
    {
        if(top==-1)
        {
            cout<<"underflow"<<endl;
            return -1;
        }
        int x=arr[top];
        top--;
        return x;
    }
    int topa()
    {
        if(top==-1)
        {
            cout<<"stack is empty";
            return -1;
        }
        return arr[top];
    }
};
int main()
{
    mystack s(5);
    s.push(1);
    s.push(2);
    cout<<s.topa();
}