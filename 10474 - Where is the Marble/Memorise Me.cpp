#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main() {
	int num,q, i, m, k;
	//scanf("%d",num);
	cin >> num;										// Reading input from STDIN
	int arr[num];
	//cout << "Input number is " << num << endl;


	for (i = 0; i<num; i++){
		cin >> arr[i];
	}
    cin >> q;
	for (i = 0; i < q; i++){
	    cin >> m;
	    k = 0;
	    for (int j = 0; j< num;j++){
	        if (m == arr[j])
	            k+=1;

	    }
	    if (k==0){
            printf("%s\n", "NOT PRESENT");
	    }
	    else
            cout << k << endl;
	}
	//cout << "Input number is " << num << endl;		// Writing output to STDOUT
}
