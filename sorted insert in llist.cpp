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
    while(temp!=NULL && data>temp->data)
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
int middle(node* head)
{
    if(head==NULL)
    return 0;
    if(head->next==NULL)
    {
        return 0;
    }
    node* temp=head,*temp1=head;
    while(temp1!=NULL&&temp1->next!=NULL&&temp!=NULL)
    {
        cout<<"a";
        temp=temp->next;
        temp1=temp1->next->next;
    }
    return temp->data;
}
node* removdup(node* head)
{
    if (head==NULL||head->next==NULL)
    return head;
    node* temp=head;
    node* temp1=head;
    while(temp->next!=NULL)
    {
        // cout<<"a";
        if (temp->data==temp->next->data)
        {
            temp->next=temp->next->next;
        }
        else{
            temp=temp->next;
        }

    }
    return head;
}
node* revgrp(node* head,int i)
{
    if(head==NULL||head->next==NULL)
    return head;
    int cunt=0;
    node*curr=head,*prev=NULL,*nex=head;
    while(curr!=NULL&&cunt<i)
    {
        nex=curr->next;
        curr->next=prev;
        prev=curr;
        curr=nex;
        cunt+=1;
    }
    node* ptr=revgrp(curr,i);
    head->next=ptr;
    return prev;

}
bool detectloop(node* head)
{
    if(head==NULL||head->next==NULL)
    return false;
    node* temp=head,*temp1=head;
    while(temp1!=NULL&&temp1->next!=NULL&&temp!=NULL)
    {
        // cout<<"a";
        temp=temp->next;
        temp1=temp1->next->next;
        if(temp==temp1)
        {
            return true;
        }
    }
    return false;
}
node* mergesort(node*h1,node* h2)
{
    if (h1==NULL&&h2==NULL)
    return NULL;
    if(h1==NULL)
    return h2;
    if(h2==NULL)
    return h1;
    node* ptr=new node(-1);
    node* temp=ptr;
    while(h1!=NULL && h2!=NULL)
    {
        if (h1->data<h2->data)
        {
            ptr->next=h1;
            ptr=h1;
            h1=h1->next;
        }
        else{
            ptr->next=h2;
            ptr=h2;
            h2=h2->next;
        }
    }
    if(h1==NULL)
    {
        while(h2!=NULL)
        {
            ptr->next=h2;
            ptr=h2;
            h2=h2->next;
        }
    }
    if(h2==NULL)
    {
        while(h1!=NULL)
        {
            ptr->next=h1;
            ptr=h1;
            h1=h1->next;
        }
    }
    temp=temp->next;
    return temp;
}
int main()
{
    node* head=NULL;
    head=sortinsert(head,7);
    // head=sortinsert(head,7);
    head=sortinsert(head,10);
    head=sortinsert(head,3);
    head=sortinsert(head,14);
    head=sortinsert(head,18);
    // head=sortinsert(head,4);

    // print(head);
    // head=revgrp(head,3);
    // detectloop(head)?cout<<"yes":cout<<"no";
    print(head);
     cout<<endl;
    node*head1=NULL;
    head1=sortinsert(head1,25);
    head1=sortinsert(head1,20);
    head1=sortinsert(head1,8);
    print(head1);
     cout<<endl;
    node* temp=mergesort(head,head1);
    print(temp);

}