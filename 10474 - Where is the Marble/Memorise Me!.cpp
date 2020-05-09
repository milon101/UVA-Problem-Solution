#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main() {
	int num,q, i, m, k, b;
	scanf("%d", &num);
	//cin >> num;										// Reading input from STDIN
	int arr[num], arrr[1005];
	//cout << "Input number is " << num << endl;
	for (i=0; i<1005; i++ )
    {
        arrr[i] = 0;
    }



	for (i = 0; i<num; i++){
		scanf("%d", &b);
		arrr[b] +=1;
	}


    scanf("%d",&q);
	for (i = 0; i < q; i++){
	    scanf("%d", &m);
	    if (arrr[m]==0){
            printf("%s\n", "NOT PRESENT");
	    }
	    else
            printf("%d\n",arrr[m]);
	}
	//cout << "Input number is " << num << endl;		// Writing output to STDOUT
}
