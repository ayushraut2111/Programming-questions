#include<stdio.h>
int main()
{
    FILE * fp;
    fp=fopen("new.txt","r");
    // fprintf(fp,"%s","Hi i am ayush chaurasia");
    char buff[256];
    fscanf(fp,"%s",buff);
printf("%s",buff);
    fclose(fp);
}