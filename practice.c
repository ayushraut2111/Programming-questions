//WAP to add a node with   data-x at the end of the given sinly linked list::

#include<stdio.h>
#include<stdlib.h>
#define pf printf

//create a data type
struct node
{
    int data;
    struct node *next;

};
struct node* CreateLinkList(int n)
{
    struct node *s = (struct node *)malloc(sizeof(struct node));
    struct node *tmp =   (struct node *)malloc(sizeof(struct node));
   
    
    if(n==0)

    {
        pf("Memory cant be allocated because linked list in empty right now..");
        free(s);
        free(tmp);
        return NULL;
    }

    else{
        
    int d1;
    
    pf("Enter the first  value(int type): ");
    scanf("%d",&d1);
    
    s->data = d1;
    s->next = NULL;
    tmp = s;
        for(int i=2;i<=n;i++)
        {
            int n_d;
            pf("Enter the data(int type): ");
            scanf("%d",&n_d);

            struct node *new;
            new = (struct node *)malloc(sizeof(struct node));   
            new->data =  n_d;
            tmp->next = new;
            new->next = NULL;
            tmp = tmp->next;
        
        }
    }
    return s;
}

struct node* ADDnode (struct node *s,int x)
{
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = x;
    ptr->next = NULL;

    //If linked list is empty
    if(s==NULL)
    {
       s= ptr;
       return s;
    }
  //create a link
  struct node* s1 = (struct node*)malloc(sizeof(struct node));
  s1 = s;
  while(s1->next!=NULL)
  {
    s1 =s1->next;
  }
  s1->next=ptr;

  //Deallocate the memory..
//   free(ptr);
  return s;


}

void Display(struct node *s)
{
   
    if(s==NULL)
    {
        pf("Linked list is Empty here....\n");
    }

    pf("Now finally our linked list is ready:\n");
    
    while(s!=NULL)
    {
        pf("%d\n",s->data);
        s = s->next;

    }
  

}

int main()
{
    int n,x;

    pf("Enter the number of node: \n");
    scanf("%d",&n);

    pf("Enter the value of x(int type): \n");
    scanf("%d",&x);

    struct node *add = CreateLinkList(n);
    struct node *address=ADDnode(add,x);
    Display(address);
}
