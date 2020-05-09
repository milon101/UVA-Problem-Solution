#include <iostream>

using namespace std;

int main() {
	int num,q, i, m, k;
	cin >> num;										// Reading input from STDIN
	int arr[num];
	cout << "Input number is " << num << endl;
	cin >> q;
	for (i = 0; i < q; i++){
	    cin >> m;
	    k = 0;
	    for (int j = 0; j< num;j++){
	        if (m == arr[j])
	            k+=1;
	    	cout << k << endl;
	    }
	}
	cout << "Input number is " << num << endl;		// Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
// Write your code here
