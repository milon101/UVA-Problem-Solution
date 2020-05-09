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
    scanf("%d", &a);
    if (a==0){
        scanf("%d",&b);
        if (arr[b] == 1)
            arr[b] = 0;
        else
            arr[b] = 1;
    }
    else
    {
        scanf("%d %d",&c,&d);
        int j=0;
        for (int i = c-1;i<d;i++){
            num += arr[i] * pow(2,j);
            j+=1;
        }
        printf("%d",num);
    }

    //printf("%d %d",n,q);

}
