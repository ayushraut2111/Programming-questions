#include<stdio.h>
int main()
{
    FILE * fp;
    fp=fopen("new.txt","w");
    fprintf(fp,"%s","Hi i am ayush chaurasia");
    fclose(fp);
}