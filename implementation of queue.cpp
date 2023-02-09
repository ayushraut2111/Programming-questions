#include<bits/stdc++.h>
#define ll long long
using namespace std;
struct myqueue{
    int* arr;
    int cap;
    int size;
    myqueue(int x)
    {
        cap=x;
        size=0;
        arr=new int[cap];
    }
    void push(int x)
    {
        if(size==cap)
        {
            cout<<"queue is full"<<endl;
            return ;
        }
        arr[size]=x;
        size++;
    }
    int pop()
    {
        if(size==0)
        {
            cout<<"queue is empty"<<endl;
            return -1;
        }
        int x=arr[0];
        for(int i=0;i<size-1;i++)
        arr[i]=arr[i+1];
        size--;
        return x;
    }
    int top()
    {
        int x=size==0?-1:arr[0];
        return x;
    }
};
int main()
{
    myqueue q(10);
    q.push(1);
    q.push(2);
    cout<<q.pop();
}