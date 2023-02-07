#include<bits/stdc++.h>
#define ll long long
using namespace std;
struct myhash{
    int *arr;
    int n;
    myhash(int i)
    {
        n=i;
        arr=new int[n];
        for(int i=0;i<n;i++)
        arr[i]=NULL;
    }
    int key(int x)
    {
        return x%n;
    }
    void insert(int x)
    {
        int k=key(x);
        if(arr[k]==NULL||arr[k]==-1)
        {
            arr[k]=x;
            return ;
        }
        int key1=k;
        k=(k+1)%n;
        while(arr[k]!=NULL&&arr[k]!=-1&&k!=key1)
        {
            k=(k+1)%n;
        }
        if(k==key1)
        {
            cout<<"hashtable is full"<<endl;
            return ;
        }
        arr[k]=x;
        return ;
    }
    void search(int x)
    {
        int k=key(x);
        if(arr[k]==x)
        {
            cout<<"found"<<endl;
            return ;
        }
        int key1=k;
        k=(k+1)%n;
        while(arr[k]!=x&&arr[k]!=NULL&&k==key1)
        {
            k=(k+1)%n;
        }
        if(arr[k]==x)
        {
            cout<<"found"<<endl;
            return ;
        }
        cout<<"not found"<<endl;
    }
    void deletehash(int x)
    {
        int k=key(x);
        if(arr[k]==x)
        {
            arr[k]=-1;
            return ;
        }
        int key1=k;
        k=(k+1)%n;
        while(arr[k]!=x&&arr[k]!=NULL&&k!=key1)
        {
            k=(k+1)%n;
        }
        if (arr[k]==x)
        {
            arr[k]=-1;
            return ;
        }
        cout<<"not found"<<endl;
    }
    void print()
    {
        for(int i=0;i<n;i++)
        {
            if (arr[i]!=NULL&&arr[i]!=-1)
            {
                cout<<arr[i]<<endl;
            }
        }
    }
};
int main()
{
    myhash mp(10);
    mp.insert(2);
    mp.insert(3);
    mp.print();
    mp.search(31);
    mp.deletehash(2);
    mp.print();
}