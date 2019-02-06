/*
 * dec2bi.cpp
 *
*/


#include <iostream>

using namespace std;

int dectoany (int liczba, int podstawa, int tab[]) {
    int i = 0;
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
        } while (liczba != 0);
    return i-1;

}

void bin2dec(int tab[]){
        ;
}

int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba; 
    cin >> podstawa;
    cout << "Wynik: " << dectoany(liczba, podstawa, tab);

    return 0;
}
