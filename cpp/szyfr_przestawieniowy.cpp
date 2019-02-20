#include <iostream>

using namespace std;

#define MAKS 100

void szyfruj_przestaw(int klucz, int ilosc, char tab[]) {
    while (ilosc % klucz != 0) {
        tab[ilosc] = '.';
        ilosc = cin.gcount() - 1;
        ilosc += 1;


        for (int i = 0; i <= ilosc; i++) {
            int szyfrowane = i + klucz;
            tab[i] = tab[szyfrowane];
            if (i + klucz > ilosc) {
                szyfrowane = szyfrowane - ilosc;
                }
            cout << tab[i];
        }
    }
}

int main(int argc, char **argv) {
    char tekst[100];
    int klucz = 0;
    int ilosc = 0;
    cout << "Podaj tekst: ";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    ilosc = cin.gcount() - 1;
    szyfruj_przestaw(klucz, ilosc, tekst);
    return 0;
}

