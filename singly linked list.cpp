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
node* insertrandom(node* head,int data,int loc)
{
    node* ptr=new node(data);
    if (head==NULL)
    {
        head=ptr;
        return head;
    }
    if(loc==1)
    {
        ptr->next=head;
        head=ptr;
        return head;
    }
    node* temp=head;
    for(int i=0;i<loc-2;i++)
    {
        temp=temp->next;
    }
    ptr->next=temp->next;
    temp->next=ptr;
    return head;
}
node* deleterandom(node* head,int loc)
{
    if (head==NULL||head->next==NULL)
    {
        return NULL;
    }
    if(loc==1)
    {
        head=head->next;
        return head;
    }
    node* ptr=head,*temp=head;
    for(int i=0;i<loc-1;i++)
    {
        ptr=temp;
        temp=temp->next;
    }
    if (temp->next==NULL)
    ptr->next=NULL;
    ptr->next=temp->next;
    return head;
}
int main()
{
    node* head=NULL;
    head=insertlast(head,1);
    head=insertlast(head,2);
    head=insertlast(head,4);
    head=insertrandom(head,3,3);
    head=deleterandom(head,4);
    print(head);

}