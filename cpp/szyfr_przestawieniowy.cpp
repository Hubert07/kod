#include <iostream>

using namespace std;

#define MAKS 100

void szyfruj_przestaw(int klucz, int ilosc, char tab[]) {
    if (ilosc % klucz != 0) {
        while (ilosc % klucz != 0) {
        tab[ilosc] = '.';
        //~ilosc = cin.gcount() - 1;
        ilosc += 1;
        }
        cout << endl;
    }


    for (int i = 0; i < ilosc; i++) {

        int szyfrowane = i + klucz;

        if (i + klucz > ilosc - 1) {
            szyfrowane -= ilosc;
        }
        cout << tab[szyfrowane];
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

