#include <iostream>

using namespace std;

// x0 = 1 dla x <> 0
float potega_rek(float x, int n) {
    if (n == 0) return 1;
    return potega_rek(x, n-1) * x;
}

int main(int argc, char **argv) {
    float podstawa;
    int wykladnik;
    cout << "Podaj podstawę: ";
    cin >> podstawa;
    cout << "Podaj wykładnik: ";
    cin >> wykladnik;
    cout << "Potęga: " << potega_rek(podstawa, wykladnik);
    return 0;
}

