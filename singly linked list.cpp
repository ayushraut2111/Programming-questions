#include<bits/stdc++.h>
#define ll long long
using namespace std;
struct node{
    int data;
    node* next;
    node(int x)
    {
        data=x;
        next=NULL;
    }
};
node* insertbegin(node* head,int x)
{
    node* ptr=new node(x);
    if(head==NULL)
    {
        head=ptr;
        return head;
    }
    ptr->next=head;
    head=ptr;
    return head;

}
void print(node* head)
{
    while(head!=NULL)
    {
        cout<<head->data<<endl;
        head=head->next;
    }
}
int main()
{
    node* head=NULL;
    head=insertbegin(head,1);
    head=insertbegin(head,2);
    head=insertbegin(head,3);
    print(head);

}