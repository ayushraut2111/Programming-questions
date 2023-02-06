#include<stdio.h>
#include<stdlib.h>
void pr(int *a)
{
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d ",*(a+i*3+j));
        }
        printf("\n");
    }
}
void pri(int **a)
{
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d\n",a[i][j]);
        }
    }
}
void main()
{
    // int a[10]={1,2,3,4,5,6,7,8,9,10};
    // printf("%d",*(a+1));
    // int a[3][3];
    // for(int i=0;i<3;i++)
    // {
    //     for(int j=0;j<3;j++)
    //     {
    //         scanf("%d",&a[i][j]);
    //     }
    // }
    // pr(a);
    int **a;
    a=malloc(3*sizeof(int)); //rows=3
    for (int i=0;i<3;i++)
    {
        a[i]=malloc(3*sizeof(int)); //column=3
        for(int j=0;j<3;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    pri(a);


}