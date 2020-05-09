#include<stdio.h>
#include<iostream>
#include <cmath>

using namespace std;

int main(){
    int n , q, arrr[5],a,b,c,d,num = 0;
    scanf("%d %d",&n, &q);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for (int i=0;i<q;i++)
    {
        scanf("%d", &a);
        if (a==1){
            scanf("%d",&b);
            if (arr[b-1] == 1)
                arr[b-1] = 0;
            else
                arr[b-1] = 1;
        }
        else
        {
            scanf("%d %d",&c,&d);
            //printf("%d %d",c,d);
            int j=0;
            for (int i = c-1;i<d;i++){
                num += arr[i] * pow(2,j);
                j+=1;
                //printf("%d %d %d\n",num,j,arr[i]);
            }
            if (num%2 == 0){
                printf("EVEN");
            }
            else{
                printf("ODD");
        }
            //printf("%d",num);
        }
    }


    //printf("%d %d",n,q);

}
