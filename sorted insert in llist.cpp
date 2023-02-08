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
void print(node* head)
{
    while(head!=NULL)
    {
        cout<<head->data<<endl;
        head=head->next;
    }
}
node* insertlast(node* head,int data)
{
    node* ptr =new node(data);
    if(head==NULL)
    {
        head=ptr;
        return head;
    }
    node* temp=head;
    while(temp->next!=NULL)
    temp=temp->next;
    temp->next=ptr;
    return head;
}
node* sortinsert(node* head,int data)
{
    node* ptr=new node(data);
    if(head==NULL)
    {
        head=ptr;
        return head;
    }
    if (data<=head->data)
    {
        ptr->next=head;
        head=ptr;
        return head;
    }
    node* temp=head,*temp1=head;
    while(temp!=NULL && data<temp->data)
    {
        temp1=temp;
        temp=temp->next;
    }
    ptr->next=temp1->next;
    temp1->next=ptr;
    return  head;

}
node* revlist(node* head)
{
    node*curr=head,*prev=NULL,*nex=head;
    while(curr!=NULL)
    {
        nex=curr->next;
        curr->next=prev;
        prev=curr;
        curr=nex;
    }
    return prev;
}
int main()
{
    node* head=NULL;
    head=sortinsert(head,7);
    head=sortinsert(head,1);
    head=sortinsert(head,3);
    head=revlist(head);
    print(head);

}