//reverse the s.l.l using last node at the last .Time Complexity = o(n^2);

#include<stdio.h>
#include<stdlib.h>
#define pf printf

struct node{
    int data;
    struct node* next;
    
    
};

struct node* Createll(int n)
{
    int d;
    struct node* s=(struct node*)malloc(sizeof(struct node));
    struct node* tmp=(struct node*)malloc(sizeof(struct node));
    
    if(n==0)
    { 
        s = NULL;
        return s;
        
        
    }
    
    pf("Enter the first value: ");
    scanf("%d",&d);
    s->data = d;
    s->next = NULL;
    tmp = s;

    for(int i=2;i<=n;i++)
    {
        int d1 ;
        struct node* new = (struct node*)malloc(sizeof(struct node));
        pf("Enter the rest data: ");
        scanf("%d",&d1);
        new->data = d1;
        new->next = NULL;
        tmp->next = new;
        tmp = tmp->next;


    }
    return s;

}

//code for reverse of the linked list

struct node* ReverseNode(struct node* s)
{
    struct node *f=NULL,*p=s,*s1,*q,*a,*temp;
    int count=0;
    while(temp!=NULL)
    {
        count++;
        temp=temp->next;
    }
    while(count--&&s!=NULL)
    {
       s1 = s;
        while(s1->next!=NULL) 
        { 
        // printf("%d",s1->data);
            p=s1;
            s1 = s1->next;
        }
        p->next = NULL;
        //linking part:
        if(f==NULL)
        {
            f=s1;
            q = s1;
        
        }
        else{
        f->next = s1;
        f = s1;
        }
        // s=s->next; 
    }
   return q;
}



int Display(struct node*s)
{
    if(s==NULL)
    {
        pf("LINKED LIST IS EMPTY..What can you reverse..");
        return 0;
    }

        pf("\n---------------------------Reversed LINKED LIST---------------------------\n");
        while(s!=NULL)
        {
            pf("%d\n",s->data);
            s = s->next;
          
        }
        return 0;

}
int main()
{
    int node;
    pf("Enter the number of node you want to create linked list: ");
    scanf("%d",&node);
    struct node*add = Createll(node);
    struct node*address=ReverseNode(add);
    Display(address);
}