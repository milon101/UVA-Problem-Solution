#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
    string inp;
    while (getline(cin, inp)) {
        for (char c : inp) {
            int ascii = (int) c;
            cout << (char) (ascii-7);
        }
        cout << endl;
    }
}
