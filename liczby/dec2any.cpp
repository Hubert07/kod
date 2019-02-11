
/*
 * dek2any.cpp
 */


#include <iostream>
#include <math.h>

using namespace std;

int cyfry[16] = {0,1,2,3,4,5,6,7,8,9,65,66,67,68,69,70};

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


void anytodec (int tab[]) {
    int podstawa = 0;
    do {
        cout << "\nPodstawa [2,16]: ";
        cin >> podstawa;
        } while (podstawa < 2 || podstawa > 16);

        int ile = 0;
        cout << "Ile cyfr? ";
        cin >> ile;
        for (int i = 0; i < ile; i++) {
            do {

                cout << "Podaj cyfrę[0-" << podstawa - 1 << "]: ";
                cin >> tab[i];
                
        // zamiana liter w odpowiednie liczby
                if ((int)tab[i] > 60) {
                    tab[i] = (int)tab[i] - 55;
                }

            } while (tab[i] < 0 || tab[i] > podstawa - 1);
        }
        // konwersja

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
        if (podstawa > 10 && tab[i] > 10)
            cout << (char)cyfry[tab[i]];
        else
            cout << tab[i];
        i--;
    }
    anytodec(tab);

    return 0;
}
