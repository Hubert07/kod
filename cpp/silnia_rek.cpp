#include <iostream>

using namespace std;

// x0 = 1 dla x <> 0
int silnia_rek(float x) {
    if (x == 0) return 1;
    return silnia_rek(x-1) * x;
}

int main(int argc, char **argv) {
    int podstawa;
    cout << "Podaj liczbę całkowitą, nieujemną: ";
    cin >> podstawa;
    cout << "Silnia: " << silnia_rek(podstawa);
    return 0;
}

