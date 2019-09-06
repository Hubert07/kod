#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    int a, b, c = 0;
    cout << "Podaj trzy liczby: ";
    cin >> a;
    cin >>b;
    cin >>c;
    if (a > b and a > c) {
        cout << "Największa liczba to: " << a;
        }
    if (c > b and c > a) {
        cout << "Największa liczba to: " << c;
        }
    if (b > a and b > c) {
        cout << "Największa liczba to: " << b;
        }

	return 0;
}

