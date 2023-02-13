#include<stdio.h>
void main()
{
    int a=23;
    int* ptr=&a;
    int **x=&ptr;
    printf("%d",**x);
}