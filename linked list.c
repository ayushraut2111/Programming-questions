#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
};
struct node* insertbegin(struct node* head,int data)
{
    struct node* ptr=(struct node*)malloc(sizeof(struct node));
    ptr->data=data;
    ptr->next=NULL;
    if(head==NULL)
    {
        head=ptr;
        return head;
    }
    ptr->next=head;
    head=ptr;
    return head;
}
void print(struct node* head)
{
    while(head!=NULL)
    {
        printf("%d\n",head->data);
        head=head->next;
    }

}
int main()
{
    struct node* head=NULL;
    head=insertbegin(head,1);
    head=insertbegin(head,2);
    head=insertbegin(head,3);
    print(head);
}