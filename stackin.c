#include<stdio.h>
int stack[100],i,ch, n, a, top;
void push()
{
int a;
if(top == n)
printf("stack full");
else
{
printf("enter the number");
scanf("%d",&a);
top=top+1;
stack[top]=a;
}
}
void pop()
{
if(top == -1)
printf("stack is empty");
else
top=top-1;
}
void show()
{
for(i=top;i>=0;i--)
{
printf("%d",stack[i]);
}}
void main()
{
printf("enter the no of elements");
scanf("%d",&a);
while(ch!=4)
{
printf("\n 1.push \n 2.pop \n 3.show\n 4.exit");
printf("enter ch");
scanf("%d", &ch);
switch(ch)
{
case 1:
{
push();
break;
}
case 2:
{
pop();
break;
}
case 3:
{
show();
break;
}
default:
{
printf("invalid entry");
}
}
}
}
