#include <iostream>

using namespace std;

void lpierwsza(int n) {
    int i = 2;
    if (n % i == 0) {
        cout << "Liczba złożona";
    }
    while (n % i != 0) {
                 i++;
    3}
    if (i * i > n) {
        cout << "Liczba pierwsza";
    }
}

int main(int argc, char **argv) {
    int n;
    cout << "podaj liczbę: ";
    cin >> n;
    lpierwsza(n);
    return 0;
}

