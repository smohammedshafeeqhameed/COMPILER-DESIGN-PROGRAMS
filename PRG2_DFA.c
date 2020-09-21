#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    int n,i, c=0,s,table[30][30],j,nt[20],f,k,r=0,p,l;
    int stre[30];
    printf("enter the number of states\n");  
    scanf("%d",&s);
    printf("enter the number of non terminals\n");
    scanf("%d",&n);
    printf("enter the non terminals\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&nt[i]);
        
    }
    printf("enter the values of dfa table\n");
    for(i=0;i<s;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("when Q%d accepts %d \n",i,nt[j]);
            printf("Q");
            scanf("%d",&table[i][j]);
        }
    }
    printf("THE DFA TABLE IS : \n");
     for(i=0;i<s;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("Q%d ",table[i][j]); 
            
        }
        printf("\n");
    }
    printf("enter the final state Q");
    scanf("%d",&f);
    printf("\nenter the length of input string: \n");
    scanf("%d",&l);
    printf("\nenter the input string: \n");
    for(i=0;i<l;i++)
    {
        scanf("%d",&stre[i]);
    }
    for(p=0;p< l;p++)
    {
      k = stre[p];

        for(j=0;j<n;j++)
        {
            if(k==nt[j])
            {  

                   r=table[r][k];
                   break;
                
            }
        }
      
      if(r==f)
      {
          break;
      }
        
    }
    
    if(r==f)
    {
        printf("the string is accepted\n");
    }
    else
    {
        printf("not accpeted\n");
    }
        
    return 0;
}
