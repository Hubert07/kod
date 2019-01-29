/*
 *
 * wyszukaj.cpp
 *
 */


#include <iostream>

using namespace std;

void wyswietl(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout<< tab[i] << " ";
    }
}


void wypelnij_los(int tab[], int roz) {
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < roz; i++) {
        tab[i] = rand() % 51;
    }
}


void sort_insert(int tab[], int roz) {
    cout << endl << "\nSortowanie przez wstawianie\n";
    int i, j, tmp;
    int licznik = 0;
    for(i = 1; i < roz; i++) { // pętla wybiera kolejne elementy zaczynając do 2
    tmp = tab[i];
    j = i - 1;
    while (j >= 0 && tab[j] > tmp) {
        tab[j+1] = tab[j];
        j--;
        licznik ++;
        }
    tab[j+1] = tmp;
    }
    cout << "liczba powtórzeń: " << licznik << endl;
}


int szukaj_bin_it(int tab[], int roz, int szuk) {
    int p, k, s;
    p = 0; k = roz -1;
    while (p <= k) {
        s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
        }
    return -1;
}


int main(int argc, char **argv)
{
    int roz = 20;
    int tab[roz];
    wypelnij_los(tab, roz);
    wyswietl(tab, roz);
    sort_insert(tab, roz);
    wyswietl(tab, roz);
    int szuk = 0;
    cout << "\nPodaj liczbę: ";
    cin >> szuk;
    int indeks = szukaj_bin_it(tab, roz, szuk);
    if (indeks >= 0)
        cout << "\nZnaleziona!" << indeks << endl;
    else
        cout << "\nMieznaleziona!" << indeks << endl;

    return 0;
}

