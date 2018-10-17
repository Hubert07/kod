#include <iostream>

using namespace std;

int liczby2() {
    int ile = 0;
    for (int i = 1; i <= 9; i++) {
        for (int j = 0; j <= 9; j++) { 
            if (i != j) {
                cout << i << j << " ";
                ile++;
                }
            }
        }
     return ile;
}

int liczby3() {
    int ile2 = 0;
    for (int i = 1; i <= 9; i++) {
        for (int j = 0; j < 10; j++) {
            if (i != j) {
                for (int k = 0; k < 10; k++) {
                    if (i != k && j != k) {
                        cout << i << j << k << " ";
                        ile2 ++;
                        }
                    }
            }
        }
    }
    return ile2;
}

int main(int argc, char **argv) {
    
    int ile = liczby2();
    cout << "\n\nLiczb dwucyfrowych: " << ile << endl;
    int ile2 = liczby3();
    cout << "\n\nLiczb trzycyfrowych jest: " << ile2;
    
// \n\n oznacza znak nowej lini
	return 0;
}

