
/*
 * dek2any.cpp
 */


#include <iostream>
#include <math.h>

using namespace std;

int dectoany(int liczba, int podstawa, int tab[]){
    int i = 0;
    do {
       tab[i] = liczba % podstawa;
       liczba = liczba / podstawa;
       i++;
    }while ( liczba != 0);
    return i-1;
    cout << endl;
}

void bin2dec(int tab[]){
        ;
}

void anytodec (int tab[]) {
    int podstawa = 0;
    do {
        cout << "\nPodstawa [2,9]: ";
        cin >> podstawa;
        } while (podstawa < 2 || podstawa > 9);

        int ile = 0;
        cout << "Ile cyfr? ";
        cin >> ile;
        for (int i = 0; i < ile; i++) {
            do {

                cout << "Podaj cyfrę[0-" << podstawa - 1 << "]: ";
                cin >> tab[i];

            } while (tab[i] < 0 || tab[i] > podstawa - 1);
        }
        // konwersja
        // 123(6) = 1 * 6^2 + 2 * 6^1 + 3 * 6^0
        int liczba10 = 0;
        for (int i = 0; i < ile; i++) {
        liczba10 += pow(podstawa, ile - 1 - i) * tab[i];
        }

        cout << "Wynik: " << liczba10;
}

// ZRÓB TAK, ŻEBY LITERKI ZAMIENIAŁO NA CYFRY

int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba;
    cin >> podstawa;
    int i = dectoany(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i > -1) {
        cout << tab[i];
        i--;
        }
    anytodec(tab);

    return 0;
}
