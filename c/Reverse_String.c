/*
Problem Statement:
Program to reverse a string

Author: 
https://www.github.com/ravikumark815

*/

#include<stdio.h>
#include<string.h>

void stringReverse(char*);
 
int main()
{
   char s[100];
 
   printf("Enter a string:\t");
   scanf("%s",s);
 
   stringReverse(s);
 
   printf("Reverse of the string: %s\n", s);
 
   return 0;
}
 
void stringReverse(char *s)
{
   int length, c;
   char *begin, *end, temp;
 
   length = strlen(s);
   begin  = s;
   end    = s;
 
   for (c = 0; c < length - 1; c++)
      end++;
 
   for (c = 0; c < length/2; c++)
   {        
      temp   = *end;
      *end   = *begin;
      *begin = temp;
 
      begin++;
      end--;
   }
}