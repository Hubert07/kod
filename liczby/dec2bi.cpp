/*
 * dec2bi.cpp
 *
*/


#include <iostream>

using namespace std;

void dectobin (int a, int tab[]) {
    int reszta = 0;
    int wykładnik = 0;
    for (int x = 0; x <= 8; x++) {
        if (a % 2 == 1) reszta = 1;
        else reszta = 0;
        a = a / 2;
        cout << "\n" << reszta;
        tab[x] = reszta;
    }
    for (int y = x; y = 0; y--) {
        int wykladnik = tab[y];
        int z = 2**wykladnik;
        suma = tab[y] *

        }
}


void wyswietl(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout<< tab[i] << " ";
    }
}


int main(int argc, char **argv)
{
    int a = 0;
    int rozmiar = 8;
    int tab[rozmiar];
    cout << "Podaj liczbę: ";
    cin >> a;
    dectobin(a, tab);
    cout << endl;
    wyswietl(tab, rozmiar);
    return 0;
}

