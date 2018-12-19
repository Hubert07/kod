#include <iostream>

using namespace std;

void wyswietl(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout<< tab[i] << " ";
    }
}

void zamien(int a, int b) {
    int tmp; //zmienna pomocnicza
    tmp = a;
    a = b;
    b = tmp;
}

void wypelnij_los(int tab[], int roz) {
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    for(int i = 1; i < roz; i++) {
        tab[0] = 1;
        tab[i] = rand() % 51;
    }
}

void sort_wybor(int tab[], int rozmiar) {
    cout << "\nSortowanie przez wybór";
    int k = tab[0];
    for(int j = 1; j < rozmiar; j++) {
        if(tab[j] < tab[k]) {
            tab[k] = tab[j];
        }
    }

    for(int i = 0; i < rozmiar; i++) {
            if (tab[k] < tab[i]) {
                zamien(tab[k], tab[i]);
            }
        }
}

int main(int argc, char **argv) {
    int rozmiar = 20;
    int tab[rozmiar]; // statyczna deklaracja tablicy
    wypelnij_los(tab, rozmiar);
    wyswietl(tab, rozmiar);
    sort_wybor(tab, rozmiar);
    wyswietl(tab, rozmiar);
    return 0;
}

