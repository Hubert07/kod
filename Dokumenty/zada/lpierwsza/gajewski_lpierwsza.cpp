#include <iostream>

using namespace std;

void lpierwsza(int n) {
    int i = 2;
    if (n % i == 0) {
        cout << "Liczba złożona";
    }
    while (n % i != 0) {
<<<<<<< HEAD
                 i++;
=======
        i++;
        if (i * i > n) {
            cout << "Liczba pierwsza";
    }
>>>>>>> 4c3e94ff5077d9395cd4bc78eeaf6a8432503328
    }
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

