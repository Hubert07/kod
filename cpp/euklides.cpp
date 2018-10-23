#include <iostream>

using namespace std;

int nwd_op(int a, int b){
    
    int licznik = 0;
    while (a > 0) {
    a = a % b;
    b = b - a;
    licznik++;
    }
    cout << " Powtórzenia: " << licznik << endl;
    return b;
}

int nwd_klas(int a, int b) {
    
    int licznik = 0;
    while (a != b) {
        if (a > b) {
            a = a -b;
            }
        if (a < b) {
            b = b - a;
            }
        licznik++;
        }
    cout << " Powtórzeń: " << licznik << endl;
    return a;
}

int main(int argc, char **argv) {
    
    int a, b;
    cout << "Podaj a: ";
    cin >> a;
    cout << "Podaj b: ";
    cin >>b;
    cout << "Największy wspólny dzielnik: " << nwd_op(a, b);
    cout << "Największy wspólny dzielnik: " << nwd_klas(a, b);

	return 0;
}

