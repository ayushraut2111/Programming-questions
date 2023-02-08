#include<bits/stdc++.h>
#define ll long long
using namespace std;
struct node{
    int data;
    node* next;
    node* prev;
    node(int x)
    {
        data=x;
        next=prev=NULL;
    }
};
node* insertlast(node* head,int data)
{
    node* ptr=new node(data);
    if (head==NULL)
    {
        head=ptr;
        return head;
    }
    node* temp=head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    ptr->prev=temp;
    temp->next=ptr;
    return head;
}
void printnode(node* head){while(head!=NULL){cout<<head->data<<endl;head=head->next;}}
void printrev(node* head)
{
    node* temp=head;
    while( temp->next!=NULL)
    temp=temp->next;
    while(temp!=NULL)
    {
        cout<<temp->data<<endl;
        temp=temp->prev;
    }
}
int main()
{
    node* head=NULL;
    head=insertlast(head,1);
    head=insertlast(head,2);
    head=insertlast(head,3);
    head=insertlast(head,4);
    printrev(head);

}