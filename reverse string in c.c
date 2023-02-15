#include<stdio.h>
#include<string.h>
int main()
{
    char a[50];
    scanf("%s",a);
    int n=strlen(a);
    printf("%d",n);
    
    for(int i=0;i<n/2;i++)
    {
        char x;
        x=a[i];
        a[i]=a[n-i-1];
        a[n-1-i]=x;
    }
    printf("%s",a);
}