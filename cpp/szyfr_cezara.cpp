/*
 * szyfr_cezara.cpp
 */


#include <iostream>
using namespace std;

#define MAKS 100

void szyfruj(int klucz, char tab[]) {
    klucz = klucz % 26;
    int kod = 0;
    int i = 0;
    while (tab[i] != '\0') {
        if (tab[i] == ' ') {
            cout << tab[i];
            i++;
            }

        if ((int)tab[i] <= 90) {
                kod = (int)tab[i] + klucz;
            if (kod > 90) {
                kod = kod - 26;
            }
            cout << (char)kod;
            i++;
            }

        if ((int)tab[i] > 96) {
            kod = (int)tab[i] + klucz;
            if (kod > 122) {
                kod = kod - 26;
            }
            cout << (char)kod;
            i++;
        }
    }
}


int main(int argc, char **argv)
{
    char tekst[100];
    int klucz = 0;
    cout << "Podaj tekst: ";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(klucz, tekst);
    return 0;
}

