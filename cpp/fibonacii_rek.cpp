#include <iostream>

using namespace std;

int fibonacci_rek(int n) {
    int a = 0;
    int b = 1;
    if (n < 1) return a;
    if (n < 2) return b;
    return fibonacci_rek(n-1) + fibonacci_rek(n-2);
    }

int main(int argc, char **argv) {
    int numer;
    cout << "Podaj numer liczby: ";
    cin >> numer;
    cout << "Wynosi: " << fibonacci_rek(numer) << endl;
    for (int i=0; i <= numer; i++) {
        cout << fibonacci_rek(i) << " ";
        if (i < 2) continue;
        else {
            cout << (float)fibonacci_rek(i) / (float)fibonacci_rek(i-1) << endl;
            }
        }
    return 0;
}

