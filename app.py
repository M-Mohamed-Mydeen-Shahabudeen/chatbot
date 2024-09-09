#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node*next;
};
struct node*top=NULL,*p,*Newnode;
int stack()
{
    top=(struct node*)malloc(sizeof(struct node));
    printf("Enter Data:");
    scanf("%d",&top->data);
    top->next=NULL;
}
int push()
{

    Newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter Data:");
    scanf("%d",&Newnode->data);
    Newnode->next=top;
    top=Newnode;
}
int pop()
{

    if(top==NULL)
    {
        printf("t\nStack is Empty");
        return 0;
    }
    else
    {
        p=top;
        printf("\nThe Element %d Is Popped From stack",p->data);
        top=top->next;
        free(p);

    }
}
int peek()
{
    if(top==NULL)
    {
        printf("\nStack Is Empty");
    }
    printf("\nPeek Of Stack is %d",top->data);
}
int peep()
{
    p=top;
    if(top==NULL)
    {
        printf("Stack Is Empty");
    }
    else
    {
        while(p!=NULL)
        {
            printf("%d",p->data);
            p=p->next;
        }
    }

}
int display()
{
    peep();
}
int count()
{
    int c=0;
    p=top;
    while(p!=NULL)
    {
        c++;

        p=p->next;
    }
    printf("Number Element in Stack: %d",c);
}
int sum()
{
    int n, s=0;
    p=top;
    while(p!=NULL)
    {
        n=p->data;
        s+=n;
        p=p->next;
    }
    printf("Sum Of Element in Stack : %d",s);
}
int search_n;
int search(int x)
{

    int value=0;
    p=top;
    while(p!=NULL)
    {
        if(p->data==x)
        {

            value+=1;
        }
        p=p->next;
    }
    if(value==1)
    {
        printf("Search Element %d  is found From Stack",x);
    }
    else
    {
        printf("\n Not Found");
    }
}

int main()
{
    int choice;
    do
    {
        printf("\n 1.Create");
        printf("\n 2.Push");
        printf("\n 3.Pop");
        printf("\n 4.Peek");
        printf("\n 5.Peep");
        printf("\n 6.Display");
        printf("\n 7.Count");
        printf("\n 8.Sum");
        printf("\n 9.Search");
        printf("\n 0.Exit");
        printf("\nEnter Your Choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            stack();
            break;
        case 2:
            push();
            break;
        case 3:
            pop();
            break;
        case 4:
            peek();
            break;
        case 5:
            peep();
            break;
        case 6:
            display();
            break;
        case 7:
            count();
            break;
        case 8:
            sum();
            break;
        case 9:

            printf("Enter Search Element:");
            scanf("%d",&search_n);
            search(search_n);
            break;
        case 0:
            printf("Exiting...\n");
            break;
        default:
            printf("Invalid choice. Please try again.\n");
            break;
        }
    }
    while(choice!=0);

}