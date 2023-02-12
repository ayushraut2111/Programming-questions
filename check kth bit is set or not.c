#include<stdio.h>
void main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    if(x&(1<<y-1)!=0)
    printf("yes");
    else
    printf("no");
    
}