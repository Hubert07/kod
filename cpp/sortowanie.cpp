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

void zamien(int &a, int &b) {
    int tmp; //zmienna pomocnicza
    tmp = a;
    a = b;
    b = tmp;
    //~cout << a << " " << b;
    // &x oznacza nie kopia a oryginał
}

void zamien2(int tab[], int &i) {
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
}

void wypelnij_sort(int tab[], int roz) {
    cout << "\nSortowanie bąbelkowe";
    int licznik = 0;
    for(int j = roz - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            licznik++;
            while (tab[i] < tab[i+1])
                zamien(tab[i], tab[i+1]);
        }
    }
    cout << "liczba powtórzeń: " << licznik << endl;
}

void sort_insert(int tab[], int roz) {
    cout << "\nSortowanie przez wstawianie\n";
    int i, j, tmp;
    for(i = 1; i < roz; i++) { // pętla wybiera kolejne elementy zaczynając do 2
    tmp = tab[i];
    j = i - 1;
    while (j >= 0 && tab[j] > tmp) {
        tab[j+1] = tab[j];
        j--;
        }
    tab[j+1] = tmp;
    }
}

int main(int argc, char **argv)
{
    int rozmiar = 40;
    int tab[rozmiar]; // statyczna deklaracja tablicy
    wypelnij_los(tab, rozmiar);
    wyswietl(tab, rozmiar);
    cout << endl;
    wypelnij_sort(tab, rozmiar);
    wyswietl(tab, rozmiar);
    sort_insert(tab, rozmiar);
    wyswietl(tab, rozmiar);
    //~int a = 10;
    //~int b = 20;
    //~zamien(a, b);
    return 0;
}

