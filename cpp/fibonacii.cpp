#include <iostream>

using namespace std;

int fibonacci_it(int n) {
    int a = 0;
    int b = 1;
    if (n < 1) return a;
    else if (n < 2) return b;
    int wynik = 0;
    for (int i = 2; i <= n; i++) {
        wynik = a + b;
        a = b;
        b = wynik;
        cout << wynik << endl;
    }
    return wynik;
}

int main(int argc, char **argv) {
    int numer;
    cout << "Podaj numer liczby: ";
    cin >> numer;
    cout << "Ciąg Fibonacciego do wyrazu: " << numer <<":" << endl;
    cout << "Ciąg Fibonacciego dla: " << numer;
    cout << fibonacci_it(numer) << endl;
    return 0;
}

