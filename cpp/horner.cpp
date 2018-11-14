#include <iostream>
#include <cstdlib>
#include <math.h>

/*
 * w(x) = 3x^3 + 3x^2 + 5x + 4 => 6 mnożenia 3 dodawania
 *
 * w(x) = x(x(2x + 3) + 5) + 4 => 3 mnożenia, 3 dodawania
 * wskaźnik to taka zmienna, która przechowywuje
 * adres komórki pamięci (można go wyświetlić)
 * alokacja to rezerwacja miejsca
 * floatr mówi o typie danych przechowywanych w tablicy
*/
using namespace std;

int horner(int stopien, float tbwspol[], float x) {
    int potega;
    int a;
    int wynik = 0;
    for (int i = 0; i <= stopien; i++) {
        if (i == stopien) {
            a = x;
            }
        else {
        potega = pow(x, stopien - i);
        a = potega * tbwspol[i];
            }
        wynik = a + wynik;
    }
    return wynik;
}

void drukujw (int stopien, float tbwspol[]) {
    int i = 0;
    for (int i = 0; i < stopien; i++) {
    cout << tbwspol[i] <<"x^" << stopien - i << " + " ;
    }
    cout << tbwspol[i];
}

int main(int argc, char **argv) {

    int stopien;
    float x = 0;
    float *tbwspol; // wskaźnik każda komórka ma adres

    cout << "Podaj stopień: ";
    cin >> stopien;
    tbwspol = new float [stopien + 1];

    for (int i = 0; i < stopien; i++) {
        cout << "Podaj współczynnik przy potędze: "
             << stopien - i << ": ";
        cin >> tbwspol[i];
        }

    cout << "Podaj argument: ";
    cin >> x;
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwspol);
    cout << "\ndla x=" << x << " Wynosi: ";
    cout << endl;
    cout << horner(stopien, tbwspol, x);
    return 0;
}

